from src.db.db_config import Base
from sqlalchemy import Column, Integer, Enum, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category_id: Mapped[int] = mapped_column(foreign_key="categories.id")
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    price: Mapped[float] = mapped_column(Integer, nullable=False)
    sku: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    stock_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[bool] = mapped_column(Enum('active', 'inactive'), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    updated_at: Mapped[DateTime] = mapped_column(DateTime)