from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BaseEvent(BaseModel):
    name: str
    planned_at: datetime


class CreateEvent(BaseEvent):
    description: Optional[str]


class UpdateEvent(BaseModel):
    id: int

    name: Optional[str]
    description: Optional[str]
    planned_at: Optional[datetime]


class EventInDB(CreateEvent):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
