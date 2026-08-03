from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.models import Order


class OrderRepository:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def save(self,order:Order):
        self.session.add(order)
        await self.session.flush()
        await self.session.refresh(order)
        return order

    async def fetch_orders_by_user_id(self, user_id: int):
        statement = (
            select(Order)
            .options(selectinload(Order.order_items))
            .where(Order.user_id == user_id)
            .order_by(Order.date.desc())
        )
        result = await self.session.execute(statement)
        return result.scalars().all()