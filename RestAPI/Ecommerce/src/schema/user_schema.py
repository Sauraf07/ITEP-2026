
from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    contact: int

class UserResponse(BaseModel):
    name: str
    email: EmailStr
    contact: int