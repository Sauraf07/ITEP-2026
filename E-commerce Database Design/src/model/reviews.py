from src.db.db_config import Base
from sqlalchemy import Column, Integer, Enum, String, DateTime
from sqlalchemy.orm import Mapped,mapped_column
class Review(Base):
    __tablename__ = 'reviews'
    review_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(foreign_key="products.id")
    user_id: Mapped[int] = mapped_column(foreign_key="users.user_id")
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    updated_at: Mapped[DateTime] = mapped_column(DateTime)