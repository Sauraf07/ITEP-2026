from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base


class Product(Base):
    __tablename__ = 'product'
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title:Mapped[str] = mapped_column(String(100))
    price:Mapped[float] = mapped_column(Float)
    brand:Mapped[str] = mapped_column(String(100))
    discount_percentage:Mapped[float] = mapped_column(Float)
    category_name:Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f"Product : {self.id} : {self.title} : {self.price} : {self.brand}"