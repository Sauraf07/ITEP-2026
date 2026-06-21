from sqlalchemy.exc import SQLAlchemyError
from src.db.db_config import sessionLocal
from src.service.author_service import AuthorService
from src.model.author import Author


class AuthorMenu:

    def create_author(self):
        try:
            with sessionLocal.begin() as session:
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                country = input("Enter your country: ")
                a = Author(name=name, email=email, country=country)
                author_service = AuthorService(session)
                result = author_service.create_author(a)
                session.refresh(result)
                print("Author created successfully")

        except SQLAlchemyError as e:
            print(e)

    def list_author(self):
        try:
            with sessionLocal() as session:
                author_service = AuthorService(session)
                author_list = author_service.list_author()
        except SQLAlchemyError as e:
            print(e)



    def show_menu(self):
        while True:
            print("\n1. Create Author")
            print("2. List Authors")
            print("0. Back")

            choice = int(input("Enter Choice: "))

            if choice == 1:
                self.create_author()
            elif choice == 2:
                self.list_author()

            elif choice == 0:
                break