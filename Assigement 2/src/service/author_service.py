from src.dao.author_dao import AuthorDAO
from src.model import *

class AuthorService:
    def __init__(self,session):
        self.Author_dao = AuthorDAO(session)

    def create_author(self,a:Author):
        return self.Author_dao.create_author(a)
