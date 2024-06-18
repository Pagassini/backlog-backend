from pydantic import BaseModel, validator


class PlatformCreateDTO(BaseModel):
    name: str
    
    @validator('name')
    def check_not_empty(cls, v):
        if not v:
            raise ValueError('Field cannot be empty')
        return v