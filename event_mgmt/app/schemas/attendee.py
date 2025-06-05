from pydantic import BaseModel, EmailStr

class AttendeeCreate(BaseModel):
    name: str
    email: EmailStr

class AttendeeOut(AttendeeCreate):
    id: int
    class Config:
        orm_mode = True
