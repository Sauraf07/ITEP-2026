from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.excaption.resource_not_found_handler import ResourceNotFound
from src.models.blogs import Blogs

class BlogRepo:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def create_blog(self,blog):
        self.session.add(blog)
        await self.session.flush()
        await self.session.refresh(blog)
        return blog
    
    async def get_all_blogs(self):
        statement = select(Blogs)
        result = await self.session.execute(statement)
        return result.scalars().all()
    
    async def get_blog_by_id(self, blog_id: int):
        statement = select(Blogs).where(Blogs.id == blog_id)
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()
    
    async def delete_blog(self, blog_id: int):
        statement = select(Blogs).where(Blogs.id == blog_id)
        result = await self.session.execute(statement)
        blog = result.scalar_one_or_none()
        if blog:
            await self.session.delete(blog)
            await self.session.flush()
            return True
        raise ResourceNotFound("Resource not found")
    
    async def update_blog(self, blog_id: int, updated_blog):
        statement = select(Blogs).where(Blogs.id == blog_id)
        result = await self.session.execute(statement)
        blog = result.scalar_one_or_none()
        if blog:
            blog.title = updated_blog.title
            blog.content = updated_blog.content
            await self.session.flush()
            await self.session.refresh(blog)
            return blog
        raise ResourceNotFound("Resource not found")
    