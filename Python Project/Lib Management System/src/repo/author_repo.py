from sqlalchemy import select

from src.ResourceNotFoundExcaption.resourcenotfound import ResourceNotFoundExcaption
from src.model.author import Author


class AuthorRepo:
    def __init__(self,session):
        self.session = session

    async def create_author(self,author:Author):
        self.session.add(author)
        await self.session.flush()
        return author

    async def view_author(self):
        statement = select(Author)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def update_author(self,id:int,name:str,email:str):
        author = await self.session.get(Author,id)
        if not author:
            raise ResourceNotFoundExcaption("Author not found")
        author.name = name
        author.email = email
        await self.session.commit()
        return author
