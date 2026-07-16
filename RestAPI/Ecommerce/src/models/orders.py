from datetime import datetime

from sqlalchemy import Integer, ForeignKey, Float, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base
class Order(Base):
    __tablename__ = "orders"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    user_id:Mapped[int] = mapped_column(Integer,ForeignKey("user.id"))
    total_price:Mapped[float] = mapped_column(Numeric,default=0)
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.now())

    # user_id:Mapped["User"] = relationship("User", back_populates="orders",cascade="all,delete")
    # order:Mapped[list["Order"]] = relationship("Order", back_populates="user")