import asyncio
from src.services.reading_book_services import ReadingBookServices
from src.model.book import Book
from sqlalchemy.exc import SQLAlchemyError
from src.exception.resourcenotfound import ResourceNotFound
from src.services.book_services import BookService
from src.db.db_config import SessionLocal


async def create_book():
    try:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        total_pages = int(input("Enter total pages: "))
        status = input("Enter book status: ")
        async with SessionLocal.begin() as session:
            book_service = BookService(session)
            book = Book(title=title,author=author,total_pages=total_pages,status=status)
            create_book = await book_service.add_book(book)
            await session.refresh(book)
            print(f"Book created with ID: {create_book.id}: {create_book.title}")
    except SQLAlchemyError as e:
        print(e)

async def view_all_books():
    try:
        async with SessionLocal() as session:
            book_service = BookService(session)
            books = await book_service.view_all_books()
            for book in books:
                print(f"Book ID: {book.id}")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Total Pages: {book.total_pages}")
                print(f"Status: {book.status}")
                print("---")


    except SQLAlchemyError as e:
        print(e)

async def view_book_by_id():
    try:
        book_id = int(input("Enter book ID to view: "))
        async with SessionLocal() as session:
            book_service = BookService(session)
            book = await book_service.view_book_by_id(book_id)
            if book:
                print(f"Book ID: {book.id}")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Total Pages: {book.total_pages}")
                print(f"Status: {book.status}")
            else:
                raise ResourceNotFound("Book not found.")

    except ResourceNotFound as e:
        print(e)
    except SQLAlchemyError as e:
        print(e)
    except Exception as e:
        print(e)

async def update_book_by_id():
    try:
        book_id = int(input("Enter book ID to update: "))
        async with SessionLocal.begin() as session:
            book_service = BookService(session)
            book = await book_service.view_book_by_id(book_id)
            if book:
                title = input(f"Enter new title (current: {book.title}): ")
                author = input(f"Enter new author (current: {book.author}): ")
                total_pages = int(input(f"Enter new total pages (current: {book.total_pages}): "))
                status = input(f"Enter new status (current: {book.status}): ")

                book.title = title
                book.author = author
                book.total_pages = total_pages
                book.status = status

                await session.commit()
                print(f"Book with ID {book.id} updated successfully.")
            else:
                raise ResourceNotFound("Book not found.")
    except ResourceNotFound as e:
        print(e)
    except SQLAlchemyError as e:
        print(e)
    except Exception as e:
        print(e)

async def delete_by_id():
    try:
        book_id = int(input("Enter book ID to delete: "))
        async with SessionLocal.begin() as session:
            book_service = BookService(session)
            book = await book_service.view_book_by_id(book_id)
            if book:
                await session.delete(book)
                await session.commit()
                print(f"Book with ID {book.id} deleted successfully.")
            else:
                raise ResourceNotFound("Book not found.")
    except ResourceNotFound as e:
        print(e)
    except SQLAlchemyError as e:
        print(e)
    except Exception as e:
        print(e)

from src.model.reading_book import ReadingBook

async def add_reading_section():
    try:
        book_id = int(input("Enter book ID: "))
        async with SessionLocal.begin() as session:
            book_service = BookService(session)
            book = await book_service.view_book_by_id(book_id)
            if not book:
                raise ResourceNotFound("Book not found")
            pages_read = int(input("Enter pages read: "))
            reading = ReadingBook(pages_read=pages_read,book_id=book.id)
            session.add(reading)
            print("Reading session added successfully")

    except ResourceNotFound as e:
        print(e)
    except SQLAlchemyError as e:
        print(e)
    except Exception as e:
        print(e)

async def view_reading_section_by_book_id():
    try:
        book_id = int(input("Enter book ID: "))

        async with SessionLocal() as session:

            reading_service = ReadingBookServices(session)

            reading_sections = (
                await reading_service
                .view_reading_sections_by_book_id(book_id)
            )

            if not reading_sections:
                print("No reading sections found.")
                return

            for section in reading_sections:
                print(f"ID: {section.id}")
                print(f"Pages Read: {section.pages_read}")
                print(f"Book ID: {section.book_id}")
                print("-" * 20)
    except SQLAlchemyError as e:
        print(e)
    except Exception as e:
        print(e)
async def update_reading_section_by_id():
    try:
        section_id = int(input("Enter reading section ID to update: "))
        async with SessionLocal.begin() as session:
            reading_service = ReadingBookServices(session)
            reading_section = await reading_service.view_reading_section_by_id(section_id)
            if reading_section:
                pages_read = int(input(f"Enter new pages read (current: {reading_section.pages_read}): "))
                reading_section.pages_read = pages_read
                await session.commit()
                print(f"Reading section with ID {reading_section.id} updated successfully.")
            else:
                raise ResourceNotFound("Reading section not found.")
    except ResourceNotFound as e:
        print(e)
    except SQLAlchemyError as e:
        print(e)

async def delete_reading_section_by_id():
    try:
        section_id = int(input("Enter reading section ID to delete: "))
        async with SessionLocal.begin() as session:
            reading_service = ReadingBookServices(session)
            reading_section = await reading_service.view_reading_sections_by_book_id(section_id)
            if reading_section:
                await session.delete(reading_section)
                await session.commit()
                print(f"Reading section with ID {reading_section.id} deleted successfully.")
            else:
                raise ResourceNotFound("Reading section not found.")
    except ResourceNotFound as e:
        print(e)
    except SQLAlchemyError as e:
        print(e)

async def main():
    while True:
        print("1 to create book")
        print("2 to view all books")
        print("3 to view book by ID")
        print("4 to update book by ID")
        print("5 to delete book by ID")
        print("6 to add reading section")
        print("7 to view reading section by book ID")
        print("8 to update reading section by ID")
        print("9 to delete reading section by ID")
        print("0 to exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            await create_book()
        elif choice == 2:
            await view_all_books()
        elif choice == 3:
            await view_book_by_id()
        elif choice == 4:
            await update_book_by_id()
        elif choice == 5:
            await delete_by_id()
        elif choice == 6:
            await add_reading_section()
        elif choice == 7:
            await view_reading_section_by_book_id()
        elif choice == 8:
            await update_reading_section_by_id()
        elif choice == 9:
            await delete_reading_section_by_id()
        elif choice == 0:
            break

asyncio.run(main())