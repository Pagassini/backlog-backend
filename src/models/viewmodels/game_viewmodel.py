from datetime import datetime
from typing import List
from pydantic import BaseModel


class GameViewModel(BaseModel):
    title: str
    description: str
    platforms: List[str]
    genres: List[str]
    release_date: datetime
    developer: str
    publisher: str
