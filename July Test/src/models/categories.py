from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base


class Categories(Base):
    __tablename__ = 'categories'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    