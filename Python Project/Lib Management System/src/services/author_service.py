from sqlalchemy.orm import sessionmaker

from src.model.author import Author
from src.repo.author_repo import AuthorRepo


class AuthorService:
    def __init__(self,session):
        self.author_repo = AuthorRepo(session)

    async def create_author(self,author:Author):
        return await self.author_repo.create_author(author)

    async def view_author(self):
        return await self.author_repo.view_author()

    async def update_author(self,id:int,name:str,email:str):
        return await self.author_repo.update_author(id,name,email)


