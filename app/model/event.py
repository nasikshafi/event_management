from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database.database import Base  
class Event_table(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    max_capacity = Column(Integer, nullable=False)

class User_table(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    registered_events = Column(Integer, nullable=True)  # Store as a comma-separated string of event IDs

