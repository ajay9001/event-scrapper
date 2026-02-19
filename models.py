from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
from pydantic import BaseModel

Base = declarative_base()


# SQLAlchemy Model (Database Table)
class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    date = Column(String)
    location = Column(String)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


# Pydantic Schema (Request Body)
class EventCreate(BaseModel):
    title: str
    date: str
    location: str
    source: str
