from pathlib import Path
import shutil

from fastapi import UploadFile

from src.models.blogs import Blogs
from src.repository.bolg_repo import BlogRepo

BASE_DIR = Path(__file__).resolve().parent.parent


class BlogService:
    def __init__(self, blog_repo: BlogRepo):
        self.blog_repo = blog_repo

    async def create_blog(
        self,
        title: str,
        content: str,
        blog_image: UploadFile,
        user_id: int,
        category_id: int,
    ):
        file_path = BASE_DIR.joinpath("public", "images", blog_image.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(blog_image.file, buffer)
        await blog_image.close()

        blog = Blogs(
            title=title,
            content=content,
            image="/public/images/" + blog_image.filename,
            user_id=user_id,
            category_id=category_id,
        )
        return await self.blog_repo.create_blog(blog)

    async def get_all_blogs(self):
        return await self.blog_repo.get_all_blogs()

    async def get_blog_by_id(self, blog_id: int):
        return await self.blog_repo.get_blog_by_id(blog_id)

    async def delete_blog(self, blog_id: int):
        return await self.blog_repo.delete_blog(blog_id)

    async def update_blog(self, blog_id: int, updated_blog):
        return await self.blog_repo.update_blog(blog_id, updated_blog)
