
from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    email: str
    password: str
    username: str
    
class UserUpdateDTO(BaseModel):
    email: str
    password: str
    username: str