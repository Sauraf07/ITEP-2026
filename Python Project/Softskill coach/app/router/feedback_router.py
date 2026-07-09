from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.service.feedback_service import FeedbackService

from app.utils.auth import get_current_user
from app.model.user import User

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"]
)

service = FeedbackService()


@router.get("/")
async def get_feedback(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await service.get_feedback(
        db=db,
        user_id=current_user.id
    )