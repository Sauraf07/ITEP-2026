from pydantic import BaseModel, ConfigDict


class FeedbackResponse(BaseModel):
    grammar_score: float
    confidence_score: float
    vocabulary_score: float
    suggestions: str

    model_config = ConfigDict(from_attributes=True)