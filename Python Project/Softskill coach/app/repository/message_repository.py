from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.message import Message


class MessageRepository:

    async def create_message(
        self,
        db: AsyncSession,
        message: Message
    ):
        db.add(message)
        await db.commit()
        await db.refresh(message)
        return message

    async def get_messages(
        self,
        db: AsyncSession,
        conversation_id: int
    ):
        result = await db.execute(
            select(Message).where(
                Message.conversation_id == conversation_id
            ).order_by(Message.id)
        )

        return result.scalars().all()

    async def delete_message(
        self,
        db: AsyncSession,
        message: Message
    ):
        await db.delete(message)
        await db.commit()