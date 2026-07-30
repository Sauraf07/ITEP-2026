
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
    token: str


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    name: str
    email: EmailStr
    token: str


