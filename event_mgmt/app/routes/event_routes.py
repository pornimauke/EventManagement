from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.database import SessionLocal
from app.models.event import Event
from app.models.attendee import Attendee
from app.schemas.event import EventCreate, EventOut
from app.schemas.attendee import AttendeeCreate, AttendeeOut
from pytz import timezone

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/events", response_model=EventOut)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    event_data = Event(**event.dict())
    db.add(event_data)
    db.commit()
    db.refresh(event_data)
    return event_data

@router.get("/events", response_model=list[EventOut])
def list_events(db: Session = Depends(get_db)):
    now = datetime.now()
    return db.query(Event).filter(Event.start_time > now).all()

@router.post("/events/{event_id}/register", response_model=AttendeeOut)
def register(event_id: int, attendee: AttendeeCreate, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(404, "Event not found")

    count = db.query(Attendee).filter(Attendee.event_id == event_id).count()
    if count >= event.max_capacity:
        raise HTTPException(400, "Event full")

    existing = db.query(Attendee).filter(
        Attendee.email == attendee.email, Attendee.event_id == event_id
    ).first()
    if existing:
        raise HTTPException(400, "Already registered")

    attendee_db = Attendee(**attendee.dict(), event_id=event_id)
    db.add(attendee_db)
    db.commit()
    db.refresh(attendee_db)
    return attendee_db

@router.get("/events/{event_id}/attendees", response_model=list[AttendeeOut])
def get_attendees(event_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return db.query(Attendee).filter(Attendee.event_id == event_id).offset(skip).limit(limit).all()
