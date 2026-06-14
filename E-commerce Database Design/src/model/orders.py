from src.db.db_config import Base
from sqlalchemy import Column, Integer, Enum, String, DateTime
from sqlalchemy.orm import Mapped,mapped_column
class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, foreign_key="user.id")
    shipping_address_id: Mapped[int] = mapped_column(Integer, foreign_key="address.id")
    billing_address_id: Mapped[int] = mapped_column(Integer, foreign_key="address.id")
    total_amount: Mapped[float] = mapped_column(Integer, name='total_amount', nullable=False)
    order_date: Mapped[DateTime] = mapped_column(DateTime, name='order_date', nullable=False)
    order_status: Mapped[str] = mapped_column(Enum("pending", "processing", "shipped", "delivered", "cancelled", name="order_status_enum"), nullable=False)
    payment_method: Mapped[str] = mapped_column(Enum("credit_card", "paypal", "bank_transfer", name="payment_method_enum"), nullable=False)
    pending_status:Mapped[Enum] = mapped_column(Enum("pending", "paid","failed","refunded", name="order_status_enum"), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    updated_at: Mapped[DateTime] = mapped_column(DateTime)