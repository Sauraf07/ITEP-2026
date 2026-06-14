from sqlalchemy import Column, Integer, Enum, String, Date
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base
class Address(Base):
    __tablename__ = "address"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    user_id:Mapped[int] = mapped_column(foreign_key="user.id")
    address_type:Mapped[str] = mapped_column(Enum('shipping', 'billing'),name='address_type',nullable=False)
    name:Mapped[str] = mapped_column(String(255),name='name',nullable=False)
    address_line1:Mapped[str] = mapped_column(String(255),name='address_line1',nullable=False)
    address_line2:Mapped[str] = mapped_column(String(255),name='address_line2',nullable=False)
    city:Mapped[str] = mapped_column(String(255),name='city',nullable=False)
    state:Mapped[str] = mapped_column(String(255),name='state',nullable=False)
    postal_code:Mapped[str] = mapped_column(String(255),name='zip',nullable=False)
    country:Mapped[str] = mapped_column(String(255),name='country',nullable=False)
    phone:Mapped[str] = mapped_column(String(10),name='phone',nullable=False)
    created_at: Mapped[Date] = mapped_column(Date)
    updated_at: Mapped[Date] = mapped_column(Date)