from src.db.db_config import Base
from sqlalchemy import Column, Integer, Enum, String, DateTime
from sqlalchemy.orm import Mapped,mapped_column
class Shipment(Base):
    __tablename__ = 'shipments'
    shipment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(foreign_key="orders.order_id")
    tracking_number: Mapped[str] = mapped_column(String(100), nullable=True, unique=True)
    shipment_method: Mapped[str] = mapped_column(String(50), nullable=True)
    shipment_status: Mapped[str] = mapped_column(Enum('pending', 'shipped', 'delivered', 'returned'), nullable=False)
    shipped_at: Mapped[DateTime] = mapped_column(DateTime)
    delivered_at: Mapped[DateTime] = mapped_column(DateTime)
    created_at: Mapped[DateTime] = mapped_column(DateTime)