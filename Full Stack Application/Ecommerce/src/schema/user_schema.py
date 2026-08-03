
from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    contact: str

class UserResponse(BaseModel):
    name: str
    email: EmailStr
    contact: str
    token: str


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    contact: str
    token: str


