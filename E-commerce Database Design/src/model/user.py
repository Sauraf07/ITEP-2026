from sqlalchemy import Integer, String, Date, Enum
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base
class User(Base):
    __tablename__ = 'user'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(100),unique=True)
    password:Mapped[str] = mapped_column(String(100))
    phone:Mapped[str] = mapped_column(String(100))
    role: Mapped[str] = mapped_column(Enum("admin", "customer", name="user_role_enum"),nullable=False)
    created_at:Mapped[Date] = mapped_column(Date)
    updated_at:Mapped[Date] = mapped_column(Date)