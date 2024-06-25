from pydantic import BaseModel, Field


class PlatformViewModel(BaseModel):
    id: str = Field(..., alias='_id')
    name: str