from datetime import datetime
from typing import List, Optional
import uuid
from pydantic import BaseModel, Field


class GameModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias='_id')
    title: str
    description: str
    platform: List[str]
    genre: List[str]
    release_date: datetime
    developer: str
class GameUpdateModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    platform: Optional[List[str]]
    genre: Optional[List[str]]
    release_date: Optional[datetime]
    developer: Optional[str]