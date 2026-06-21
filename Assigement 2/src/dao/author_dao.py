from sqlalchemy import select

from src.model import *
class AuthorDAO:
    def __init__(self,session):
        self.session = session

    def create_author(self,a:Author):
        self.session.add(a)
        self.session.flush()
        return a

    def author_list(self):
        statement = select(Author)
        results = self.session.execute(statement).scalars().all()
        return results