from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class GameCreateDTO(BaseModel):
    title: str
    description: str
    platform: List[str]
    genre: List[str]
    release_date: datetime
    developer: str

class GameUpdateDTO(BaseModel):
    title: Optional[str]
    description: Optional[str]
    platform: Optional[List[str]]
    genre: Optional[List[str]]
    release_date: Optional[datetime]
    developer: Optional[str]