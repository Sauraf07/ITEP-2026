from sqlalchemy import Integer, ForeignKey, Float, Numeric
from sqlalchemy.orm import mapped_column, Mapped

from src.db.db_config import Base
class OrderItems(Base):
    __tablename__ = "orderItems"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    order_id:Mapped[int] = mapped_column(Integer,ForeignKey("orders.id"))
    product_id:Mapped[int] = mapped_column(Integer,ForeignKey("product.id"))
    quantity:Mapped[int] = mapped_column(Integer)
    price:Mapped[float] = mapped_column(Numeric)
