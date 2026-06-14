from src.db.db_config import Base
from sqlalchemy import Column, Integer, Enum, String, DateTime
from sqlalchemy.orm import Mapped,mapped_column
class Order_Items(Base):
    __tablename__ = 'order_items'
    order_item_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(foreign_key="orders.order_id")
    product_id: Mapped[int] = mapped_column(foreign_key="products.id")
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price: Mapped[float] = mapped_column(Integer, nullable=False)
    discount: Mapped[float] = mapped_column(Integer, nullable=True)
    total_price: Mapped[float] = mapped_column(Integer, nullable=False)