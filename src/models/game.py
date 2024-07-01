from datetime import datetime
from typing import List, Optional
import uuid
from pydantic import BaseModel, Field


class GameModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias='_id')
    title: str
    platforms: List[str]
    genres: List[str]
    developer: str
class GameUpdateModel(BaseModel):
    title: str
    platforms: List[str]
    genres: List[str]
    developer: str