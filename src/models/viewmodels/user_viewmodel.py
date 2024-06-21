
from pydantic import BaseModel


class UserViewModel(BaseModel):
    email: str
    username: str