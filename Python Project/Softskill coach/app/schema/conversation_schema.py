from pydantic import BaseModel, ConfigDict


# Create Conversation
class ConversationCreate(BaseModel):
    title: str


# Conversation Response
class ConversationResponse(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)