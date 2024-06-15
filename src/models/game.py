from datetime import datetime
from typing import Optional
import uuid
from pydantic import BaseModel, Field


class GameModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str
    description: str
    platform: str
    genre: str
    release_date: datetime

class GameUpdateModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    platform: Optional[str]
    genre: Optional[str]
    release_date: Optional[datetime]