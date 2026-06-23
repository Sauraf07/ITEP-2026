from sqlalchemy import select
from src.model.reading_book import ReadingBook


class ReadingBookRepo:

    def __init__(self, session):
        self.session = session

    async def add_reading_section(self, reading_section):
        self.session.add(reading_section)
        await self.session.flush()
        return reading_section

    async def view_reading_sections_by_book_id(self, book_id: int):
        statement = select(ReadingBook).where(ReadingBook.book_id == book_id)
        result = await self.session.execute(statement)
        return result.scalars().all()