from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base


class Product(Base):
    __tablename__ = "product"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String(100))
    price:Mapped[float] = mapped_column(Float)
    discount_percent:Mapped[float] = mapped_column(Float)
    brand:Mapped[str] = mapped_column(String(100))
    catagory_name:Mapped[str] = mapped_column(String(100))