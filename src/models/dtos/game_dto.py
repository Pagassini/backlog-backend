from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class GameCreateDTO(BaseModel):
    title: str
    description: str
    platform: str
    genre: str
    release_date: datetime
    developer: str

class GameUpdateDTO(BaseModel):
    title: Optional[str]
    description: Optional[str]
    platform: Optional[str]
    genre: Optional[str]
    release_date: Optional[datetime]
    developer: Optional[str]