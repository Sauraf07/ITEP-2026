from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base


class Product(Base):
    __tablename__ = 'product'
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title:Mapped[str] = mapped_column(String(100))
    