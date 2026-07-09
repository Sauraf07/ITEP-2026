from sqlalchemy.ext.asyncio import AsyncSession

from app.model.feedback import Feedback
from app.repository.feedback_repository import FeedbackRepository


class FeedbackService:

    def __init__(self):
        self.repository = FeedbackRepository()

    async def save_feedback(
        self,
        db: AsyncSession,
        grammar: float,
        confidence: float,
        vocabulary: float,
        suggestions: str,
        user_id: int
    ):

        feedback = Feedback(
            grammar_score=grammar,
            confidence_score=confidence,
            vocabulary_score=vocabulary,
            suggestions=suggestions,
            user_id=user_id
        )

        return await self.repository.create_feedback(
            db,
            feedback
        )

    async def get_feedback(
        self,
        db: AsyncSession,
        user_id: int
    ):
        return await self.repository.get_feedback_by_user(
            db,
            user_id
        )