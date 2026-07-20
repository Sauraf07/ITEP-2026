from src.models.comment import Comment
from src.repository.comment_repo import CommentRepository


class CommentService:
    def __init__(self, comment_repo: CommentRepository):
        self.comment_repo = comment_repo

    async def create_comment(self, comment_text: str, user_id: int, blog_id: int):
        comment = Comment(comment=comment_text, user_id=user_id, blog_id=blog_id)
        return await self.comment_repo.create_comment(comment)

    async def get_comments_by_blog(self, blog_id: int):
        return await self.comment_repo.get_comments_by_blog(blog_id)

    async def delete_comment(self, comment_id: int):
        return await self.comment_repo.delete_comment(comment_id)
