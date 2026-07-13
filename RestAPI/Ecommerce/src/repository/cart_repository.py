from sqlalchemy.ext.asyncio import AsyncSession


class CartRepository:
    def __init__(self,session:AsyncSession):
        self.session = session