

from pydantic import BaseModel


class PlatformCreateDTO(BaseModel):
    name: str