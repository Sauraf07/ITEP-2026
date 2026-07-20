from pydantic import BaseModel, EmailStr


class UserRequestBody(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    email:EmailStr
    token:str