from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.categories import Categories

class CategoriesRepository:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def create(self, category: Categories):
        self.session.add(category)
        await self.session.flush()
        await self.session.refresh(category)
        return category

    async def get_all_categories(self):
        statement = select(Categories)
        result = await self.session.execute(statement)
        return result.scalars().all()
    
    async def get_category_by_id(self, category_id: int):
        statement = select(Categories).where(Categories.id == category_id)
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()
    
    async def delete_category(self, category_id: int):
        statement = select(Categories).where(Categories.id == category_id)
        result = await self.session.execute(statement)
        category = result.scalar_one_or_none()
        if category:
            await self.session.delete(category)
            await self.session.flush()
            return True
        return False

    async def update_category(self, category_id: int, updated_category: Categories):
        statement = select(Categories).where(Categories.id == category_id)
        result = await self.session.execute(statement)
        category = result.scalar_one_or_none()
        if category:
            category.name = updated_category.name
            await self.session.flush()
            await self.session.refresh(category)
            return category
        return None
    