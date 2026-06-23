from sqlalchemy import select

from src.model.book import Book


class BookRepo:
    def __init__(self,session):
        self.session = session

    async def add_book(self, book: Book):
        self.session.add(book)
        await self.session.flush()
        return book
    
    async def view_all_books(self):
        statement = select(Book)
        books = await self.session.execute(statement)
        books = books.scalars().all()
        return books
    
    async def view_book_by_id(self, book_id: int):
        statement = select(Book).where(Book.id == book_id)
        book = await self.session.execute(statement)
        book = book.scalar_one_or_none()
        return book
    
    async def Update_book(self, book: Book):
        await self.session.commit()
        return book
    
    async def delete_book(self, book: Book):
        await self.session.delete(book)
        await self.session.commit()
        return book