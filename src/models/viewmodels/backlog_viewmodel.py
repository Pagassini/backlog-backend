from pydantic import BaseModel, Field
from enums.status_enum import StatusEnum


class BacklogViewModel(BaseModel):
    id: str = Field(..., alias='_id')
    game_id: str
    user_id: str
    status: StatusEnum
    