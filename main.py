from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import engine, SessionLocal
from app.models import Base, Event, EventCreate
from app.scraper import scrape_events  # 🔥 Import scraper

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Home Route
@app.get("/")
def home():
    return {"message": "Event Scraper API is running 🚀"}


# ✅ Create Event (JSON Body)
@app.post("/events")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = Event(
        title=event.title,
        date=event.date,
        location=event.location,
        source=event.source
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return {
        "message": "Event added successfully ✅",
        "event_id": new_event.id
    }
@app.get("/events")
def get_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    events = db.query(Event).offset(skip).limit(limit).all()
    return events



from sqlalchemy import or_

@app.get("/events")
def get_events(
    skip: int = 0,
    limit: int = 10,
    search: str = None,
    sort_by: str = "id",
    order: str = "asc",
    db: Session = Depends(get_db)
):
    query = db.query(Event)

    # 🔎 Search filter
    if search:
        query = query.filter(
            Event.title.ilike(f"%{search}%")
        )

    # 🔽 Sorting
    if sort_by == "title":
        column = Event.title
    elif sort_by == "date":
        column = Event.date
    else:
        column = Event.id

    if order == "desc":
        query = query.order_by(column.desc())
    else:
        query = query.order_by(column.asc())

    total = query.count()

    events = query.offset(skip).limit(limit).all()

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": events
    }
