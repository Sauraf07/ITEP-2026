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
    
    async def update_reading_section(self, reading_section: ReadingBook):
        statement = select(ReadingBook).where(ReadingBook.id == reading_section.id)
        result = await self.session.execute(statement)
        existing_section = result.scalars().all()
        if not existing_section:
            return None
        await self.session.commit()
        return reading_section
    
    async def delete_reading_sections_by_id(self, reading_section_id: int):
        statement = select(ReadingBook).where(ReadingBook.id == reading_section_id)
        result = await self.session.execute(statement)
        reading_section = result.scalars().first()
        if not reading_section:
            return None
        await self.session.delete(reading_section)
        await self.session.commit()
        return reading_section