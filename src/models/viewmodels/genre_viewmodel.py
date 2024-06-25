from pydantic import BaseModel, Field


class GenreViewModel(BaseModel):
    id: str = Field(..., alias='_id')
    name: str