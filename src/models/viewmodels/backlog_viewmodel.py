from pydantic import BaseModel
from enums.status_enum import StatusEnum


class BacklogViewModel(BaseModel):
    game_id: str
    user_id: str
    status: StatusEnum
    