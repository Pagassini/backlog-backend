from pydantic import BaseModel
from enums.status_enum import StatusEnum


class BacklogCreateDTO(BaseModel):
    game_id: str
    user_id: str
    status: StatusEnum

class BacklogUpdateDTO(BaseModel):
    status: StatusEnum