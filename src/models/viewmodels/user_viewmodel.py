
from pydantic import BaseModel, Field


class UserViewModel(BaseModel):
    id: str = Field(..., alias='_id')
    email: str
    username: str