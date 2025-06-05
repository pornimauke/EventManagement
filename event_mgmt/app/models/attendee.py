from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from app.db.database import Base

class Attendee(Base):
    __tablename__ = "attendees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))

    __table_args__ = (
        UniqueConstraint('email', 'event_id', name='unique_attendee'),
    )
