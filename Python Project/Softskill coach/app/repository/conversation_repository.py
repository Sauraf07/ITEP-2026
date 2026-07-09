from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.conversation import Conversation


class ConversationRepository:

    async def create_conversation(
        self,
        db: AsyncSession,
        conversation: Conversation
    ):
        db.add(conversation)
        await db.commit()
        await db.refresh(conversation)
        return conversation

    async def get_conversation_by_id(
        self,
        db: AsyncSession,
        conversation_id: int
    ):
        result = await db.execute(
            select(Conversation).where(
                Conversation.id == conversation_id
            )
        )

        return result.scalar_one_or_none()

    async def get_user_conversations(
        self,
        db: AsyncSession,
        user_id: int
    ):
        result = await db.execute(
            select(Conversation).where(
                Conversation.user_id == user_id
            )
        )

        return result.scalars().all()

    async def delete_conversation(
        self,
        db: AsyncSession,
        conversation: Conversation
    ):
        await db.delete(conversation)
        await db.commit()