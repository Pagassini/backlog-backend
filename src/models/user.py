import uuid
from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias='_id')
    email: str
    password: str
    username: str
    
class UserUpdateModel(BaseModel):
    email: str
    password: str
    username: str