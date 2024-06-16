from pydantic import BaseModel


class PlatformViewModel(BaseModel):
    name: str