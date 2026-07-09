from pydantic import BaseModel, EmailStr, ConfigDict


# Register Request
class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str


# Login Request
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# User Response
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)