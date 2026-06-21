import asyncio

from sqlalchemy.exc import SQLAlchemyError

from src.db.db_config import SessionLocal
from src.model import Author, author
from src.services.author_service import AuthorService

async def update_author():
    try:
        id = int(input("Enter your id: "))
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        async with SessionLocal.begin() as session:
            author = Author(id=id,name=name, email=email)
            author_service = AuthorService(session)
            author = await author_service.update_author(id, name, email)
            await session.refresh(author)
            print(f"Author updated successfully {author.id} : {author.name}")


    except SQLAlchemyError as e:
        print(e)

async def view_author():
    try:
        async with SessionLocal() as session:
            author_service = AuthorService(session)
            author_list = await author_service.view_author()
            for author in author_list:
                print(f"Author_id :  {author.id} Name : {author.name}")
    except SQLAlchemyError as e:
        print(e)

async def create_author():
    try:
        author = input("Enter your name: ")
        email = input("Enter your email: ")
        async with SessionLocal.begin() as session:
            author = Author(name=author, email=email)
            author_service = AuthorService(session)
            author = await author_service.create_author(author)
            await session.refresh(author)
            print(f"Author created successfully {author.id} : {author.name}")
    except SQLAlchemyError as e:
        print(e)

async def main():
    while True:
        print("1 To add author")
        print("2 To view all authors")
        print("3 to update author")
        print("0 to exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            await create_author()

        elif choice == 0:
            break

        elif choice == 2:
            await view_author()

        elif choice == 3:
            await update_author()

asyncio.run(main())