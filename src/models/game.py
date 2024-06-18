from datetime import datetime
from typing import List, Optional
import uuid
from pydantic import BaseModel, Field


class GameModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias='_id')
    title: str
    description: str
    platforms: List[str]
    genres: List[str]
    release_date: datetime
    developer: str
    publisher: str
class GameUpdateModel(BaseModel):
    title: str
    description: str
    platforms: List[str]
    genres: List[str]
    release_date: datetime
    developer: str
    publisher: str