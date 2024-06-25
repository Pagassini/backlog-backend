from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class GameViewModel(BaseModel):
    id: str = Field(..., alias='_id')
    title: str
    description: str
    platforms: List[str]
    genres: List[str]
    release_date: datetime
    developer: str
    publisher: str
