from pydantic import BaseModel, Field
from typing import Optional, List   
from datetime import datetime

class Event(BaseModel):
    id: Optional[int] = Field(default=None, description="Unique identifier for the event")
    name: str = Field(..., description="Name of the event")
    date: datetime = Field(..., description="Date of the event in YYYY-MM-DD format")
    location: str = Field(..., description="Location of the event")
    max_capacity: int = Field(..., description="Maximum number of attendees allowed for the event")


class User(BaseModel):
    id: Optional[int] = Field(default=None, description="Unique identifier for the user")
    name: str = Field(..., description="Name of the user")
    email: str = Field(..., description="Email address of the user")
    registered_event: int = Field(..., description="List of event IDs the user is registered for")

    