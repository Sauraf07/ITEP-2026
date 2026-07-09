from sqlalchemy.ext.asyncio import AsyncSession

from app.model.conversation import Conversation
from app.repository.conversation_repository import ConversationRepository
from app.schema.conversation_schema import ConversationCreate


class ConversationService:

    def __init__(self):
        self.repository = ConversationRepository()

    async def create_conversation(
        self,
        db: AsyncSession,
        data: ConversationCreate,
        user_id: int
    ):

        conversation = Conversation(
            title=data.title,
            user_id=user_id
        )

        return await self.repository.create_conversation(
            db,
            conversation
        )

    async def get_conversations(
        self,
        db: AsyncSession,
        user_id: int
    ):
        return await self.repository.get_user_conversations(
            db,
            user_id
        )