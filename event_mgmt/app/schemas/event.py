from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    name: str
    location: str
    start_time: datetime
    end_time: datetime
    max_capacity: int

class EventOut(EventCreate):
    id: int
    class Config:
        orm_mode = True
