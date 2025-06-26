from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session  
from app.database.database import get_db
from app.schemas.event import Event,User  # Assuming you have an Event schema defined
from app.model.event import Event_table, User_table  # Assuming you have an Event_table model defined
router = APIRouter()
@router.get("/events")
async def get_events():
    db: Session = next(get_db())   
    if not db:
        raise HTTPException(status_code=500, detail="Database connection error")  
      
    return db.query(Event_table).all()  # Fetch all events from the database

@router.post("/events")
async def create_event(event: Event):
    db: Session = next(get_db())
    if not db:
        raise HTTPException(status_code=500, detail="Database connection error")
    db_event = Event_table(name=event.name, location=event.location, date=event.date, max_capacity=event.max_capacity)
    if not event:
        raise HTTPException(status_code=400, detail="Event data is required")
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return {"message": "Event created successfully", "event": event}    

@router.post("/events/{event_id}/register")
async def register_for_event(event_id: int, user: User):
    if not user:
        raise HTTPException(status_code=400, detail="User data is required")    
    db: Session = next(get_db())
    if not db:
        raise HTTPException(status_code=500, detail="Database connection error")
    db_data = User_table(
        name=user.name,
        email=user.email,
        registered_events = user.registered_event  
    )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return {"message": f"User registered for event {event_id} successfully", "user": user}

@router.get("/events/{event_id}/attendees")
async def get_event_attendees(event_id: int):
    db: Session = next(get_db())   
    if not db:
        raise HTTPException(status_code=500, detail="Database connection error")     
    return db.query(User_table).filter(User_table.registered_events==event_id).all()  

