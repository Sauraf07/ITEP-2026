from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Order


class OrderRepository:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def create_order(self,order:Order):
        pass