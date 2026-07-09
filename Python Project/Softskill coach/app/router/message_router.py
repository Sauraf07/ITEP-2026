from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schema.message_schema import MessageCreate
from app.service.message_service import MessageService

router = APIRouter(
    prefix="/message",
    tags=["Message"]
)

service = MessageService()


@router.post("/{conversation_id}")
async def send_message(
    conversation_id: int,
    message: MessageCreate,
    db: AsyncSession = Depends(get_db)
):

    return await service.create_message(
        db=db,
        role="user",
        content=message.content,
        conversation_id=conversation_id
    )


@router.get("/{conversation_id}")
async def get_messages(
    conversation_id: int,
    db: AsyncSession = Depends(get_db)
):

    return await service.get_messages(
        db=db,
        conversation_id=conversation_id
    )