from src.db.db_config import Base
from sqlalchemy import Column, Integer, Enum, String, DateTime
from sqlalchemy.orm import Mapped,mapped_column
class Payment(Base):
    __tablename__ = 'payments'
    payment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(foreign_key="orders.order_id")
    payment_method: Mapped[str] = mapped_column(String(50), nullable=False)
    payment_status: Mapped[str] = mapped_column(Enum('pending', 'completed', 'failed','refunded'), nullable=False)
    amount: Mapped[float] = mapped_column(Integer, nullable=False)
    transaction_id: Mapped[str] = mapped_column(String(100), nullable=True)
    paid_at: Mapped[DateTime] = mapped_column(DateTime)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
 