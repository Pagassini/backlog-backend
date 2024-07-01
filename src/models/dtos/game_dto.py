from typing import List
from pydantic import BaseModel, validator


class GameCreateDTO(BaseModel):
    title: str
    platforms: List[str]
    genres: List[str]
    developer: str
    
    @validator('title', 'platforms', 'genres','developer')
    def check_not_empty(cls, v):
        if not v:
            raise ValueError('Field cannot be empty')
        return v

class GameUpdateDTO(BaseModel):
    title: str
    platforms: List[str]
    genres: List[str]
    developer: str
    
    @validator('title', 'platforms', 'genres','developer')
    def check_not_empty(cls, v):
        if not v:
            raise ValueError('Field cannot be empty')
        return v