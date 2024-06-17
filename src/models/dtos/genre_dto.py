from pydantic import BaseModel


class GenreCreateDTO(BaseModel):
    name: str