from datetime import datetime
from pydantic import BaseModel


class GameViewModel(BaseModel):
    title: str
    description: str
    platform: str
    genre: str
    release_date: datetime
    developer: str
