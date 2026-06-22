

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base


class User(Base):
    __tablename__ = 'user'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    email:Mapped[str] = mapped_column(String(100),unique=True)
    password:Mapped[str] = mapped_column(String(100))
    