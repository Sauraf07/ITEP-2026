from sqlalchemy.ext.asyncio import AsyncSession


class CartItemsRepository:
    def __init__(self,session:AsyncSession):
        self.session = session