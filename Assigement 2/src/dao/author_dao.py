from src.model import *
class AuthorDAO:
    def __init__(self,session):
        self.session = session

    def create_author(self,a:Author):
        self.session.add(a)
        self.session.flush()
        return a
