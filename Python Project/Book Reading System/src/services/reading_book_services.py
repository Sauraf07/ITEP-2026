from src.repo.reading_book_repo import ReadingBook
class ReadingBookServices:
    def __init__(self,session):
        self.reading_book_repo = ReadingBook(session)

    async def add_reading_section(self,reading_section):
        return await self.reading_book_repo.add_reading_section(reading_section)
    
    async def view_reading_sections_by_book_id(self,book_id):
        return await self.reading_book_repo.view_reading_sections_by_book_id(book_id)