from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, validator


class GameCreateDTO(BaseModel):
    title: str
    description: str
    platforms: List[str]
    genres: List[str]
    release_date: datetime
    developer: str
    publisher: str
    
    @validator('title', 'description', 'platforms', 'genres', 'release_date','developer','publisher')
    def check_not_empty(cls, v):
        if not v:
            raise ValueError('Field cannot be empty')
        return v

class GameUpdateDTO(BaseModel):
    title: str
    description: str
    platforms: List[str]
    genres: List[str]
    release_date: datetime
    developer: str
    publisher: str
    
    @validator('title', 'description', 'platforms', 'genres', 'release_date','developer','publisher')
    def check_not_empty(cls, v):
        if not v:
            raise ValueError('Field cannot be empty')
        return v