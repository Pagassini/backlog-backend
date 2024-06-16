from pydantic import BaseModel


class GenreViewModel(BaseModel):
    name: str