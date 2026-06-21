from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base
class Book(Base):
    __tablename__ = 'book'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String(100))
    price:Mapped[int] = mapped_column(Integer)
    author_id:Mapped[int] = mapped_column(ForeignKey('author.id'))