from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from models.event import Event
from schemas.event import (
    CreateEvent,
    UpdateEvent,
    EventInDB
)

event_router = APIRouter(
    prefix="/event",
    tags=['events']
)


@event_router.post('/', response_model=EventInDB)
async def create_event(new_event: CreateEvent, db: Session = Depends(get_db)):
    new_event = Event(**new_event.dict())

    db.add(new_event)
    db.commit()
    db.flush()

    return new_event


@event_router.put('/', response_model=EventInDB)
async def edit_event(event: UpdateEvent, db: Session = Depends(get_db)):
    db_event = db.query(Event).get(event.id)

    if not db_event:
        raise HTTPException(status_code=400, detail="Event not found")

    for key, value in event.dict().items():
        if getattr(db_event, key) != value and value:
            setattr(db_event, key, value)

    db.commit()
    db.flush()

    return db_event


@event_router.get('/<event_id>', response_model=EventInDB)
async def get_event_by_id(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).get(event_id)

    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    return event


@event_router.delete("/<event_id>")
async def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(Event).get(event_id)
    if db_event:
        db.delete(db_event)
        return {
            "detail": "ok"
        }
    raise HTTPException(status_code=400, detail="Event not found")
