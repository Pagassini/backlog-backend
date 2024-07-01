from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class GameViewModel(BaseModel):
    id: str = Field(..., alias='_id')
    title: str
    platforms: List[str]
    genres: List[str]
    developer: str
