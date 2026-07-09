from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.feedback import Feedback


class FeedbackRepository:

    async def create_feedback(
        self,
        db: AsyncSession,
        feedback: Feedback
    ):
        db.add(feedback)
        await db.commit()
        await db.refresh(feedback)
        return feedback

    async def get_feedback_by_user(
        self,
        db: AsyncSession,
        user_id: int
    ):
        result = await db.execute(
            select(Feedback).where(
                Feedback.user_id == user_id
            )
        )

        return result.scalars().all()

    async def delete_feedback(
        self,
        db: AsyncSession,
        feedback: Feedback
    ):
        await db.delete(feedback)
        await db.commit()