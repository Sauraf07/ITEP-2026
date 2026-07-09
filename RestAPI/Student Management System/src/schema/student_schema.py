from pydantic import BaseModel, EmailStr


class StudentReq(BaseModel):
    name: str
    email: EmailStr
    course: str
    age: int

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    course: str
    age: int