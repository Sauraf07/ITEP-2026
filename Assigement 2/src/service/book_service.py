from src.dao.book_dao import BookDAO
from src.model import *
class BookService:
    def __init__(self,session):
        self.BookDAO = BookDAO(session)