from pydantic import BaseModel, Field
import uuid
from enums.status_enum import StatusEnum


class BacklogModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias='_id')
    game_id: str
    user_id: str
    status: StatusEnum


class BacklogUpdateModel(BaseModel):
    status: StatusEnum
    
