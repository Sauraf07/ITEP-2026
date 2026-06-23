from src.model import Book
from src.repo.book_repo import BookRepo


class BookService:
    def __init__(self,session):
        self.book_repo = BookRepo(session)

    async def add_book(self,book):
        return await self.book_repo.add_book(book)
    
    async def view_all_books(self):
        return await self.book_repo.view_all_books()
    
    async def view_book_by_id(self,book_id):
        return await self.book_repo.view_book_by_id(book_id)
    
    async def update_book(self,book):
        return await self.book_repo.Update_book(book)
    
    async def delete_book(self,book):
        return await self.book_repo.delete_book(book)
    