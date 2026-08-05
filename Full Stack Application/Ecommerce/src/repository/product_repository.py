from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.models import Product, Category


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, product: Product):
        self.session.add(product)
        await self.session.flush()
        await self.session.refresh(product)
        return product

    async def fetch_all(self,page):
        limit = 5
        offset = (page - 1) * limit
        statement = (select(Product)
                     .offset(offset)
                     .limit(limit)
                     .options(selectinload(Product.category)))
        result = await self.session.execute(statement)
        return result.scalars().all()


    async def fetch_by_id(self, id: int):
        statement = (
            select(Product)
            .options(selectinload(Product.category))
            .where(Product.id == id)
        )
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def search(self,keyword: str):
        statement = select(Product).where(Product.title.ilike(f"%{keyword}%"))
        result = await self.session.execute(statement)
        return result.scalars().all()