from fastapi import FastAPI
from app.api.event_routes import router as event_router
from app.database.database import Base, engine
app = FastAPI()
print("Starting FastAPI application...")
app.include_router(
    event_router,  # Adjust the import path as necessary    
    prefix="/v1",
    tags=["events_management"],
    responses={404: {"description": "Not found"}},        
)

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the FastAPI application!"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
Base.metadata.create_all(bind=engine)
print("Database initialized successfully.")
# if __name__ == "__main__":
#     Base.metadata.create_all(bind=engine)
#     print("Database initialized successfully.")
