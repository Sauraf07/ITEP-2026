from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schema.conversation_schema import (
    ConversationCreate
)
from app.service.conversation_service import (
    ConversationService
)

from app.utils.auth import get_current_user
from app.model.user import User

router = APIRouter(
    prefix="/conversation",
    tags=["Conversation"]
)

service = ConversationService()


@router.post("/")
async def create_conversation(
    conversation: ConversationCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await service.create_conversation(
        db=db,
        data=conversation,
        user_id=current_user.id
    )


@router.get("/")
async def get_conversations(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await service.get_conversations(
        db=db,
        user_id=current_user.id
    )