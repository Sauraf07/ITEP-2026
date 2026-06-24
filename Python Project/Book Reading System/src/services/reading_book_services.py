from src.repo.reading_book_repo import ReadingBookRepo
class ReadingBookServices:
    def __init__(self,session):
        self.reading_book_repo = ReadingBookRepo(session)

    async def add_reading_section(self,reading_section):
        return await self.reading_book_repo.add_reading_section(reading_section)
    
    async def view_reading_sections_by_book_id(self,book_id):
        return await self.reading_book_repo.view_reading_sections_by_book_id(book_id)
    
    async def update_reading_section(self,reading_section):
        return await self.reading_book_repo.update_reading_section(reading_section)
    
    async def delete_reading_section_by_id(self,reading_section_id):
        return await self.reading_book_repo.delete_reading_sections_by_id(reading_section_id)