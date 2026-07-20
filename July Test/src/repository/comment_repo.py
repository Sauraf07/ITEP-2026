from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.excaption.resource_not_found_handler import ResourceNotFound
from src.models.comment import Comment


class CommentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_comment(self, comment: Comment):
        self.session.add(comment)
        await self.session.flush()
        await self.session.refresh(comment)
        return comment

    async def get_comments_by_blog(self, blog_id: int):
        statement = select(Comment).where(Comment.blog_id == blog_id)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def delete_comment(self, comment_id: int):
        statement = select(Comment).where(Comment.id == comment_id)
        result = await self.session.execute(statement)
        comment = result.scalar_one_or_none()
        if comment:
            await self.session.delete(comment)
            await self.session.flush()
            return True
        raise ResourceNotFound("Comment not found")
