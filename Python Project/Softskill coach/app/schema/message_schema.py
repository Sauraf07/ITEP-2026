from pydantic import BaseModel, ConfigDict


# Create Message
class MessageCreate(BaseModel):
    content: str


# Message Response
class MessageResponse(BaseModel):
    id: int
    role: str
    content: str

    model_config = ConfigDict(from_attributes=True)