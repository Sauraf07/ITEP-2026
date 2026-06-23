# from model.reading_book import ReadingBook
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base


class Book(Base):
    __tablename__ = "book"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String(100))
    author:Mapped[str] = mapped_column(String(100))
    total_pages:Mapped[int] = mapped_column(Integer)
    status:Mapped[str] = mapped_column(String(20))
    reading_sessions: Mapped[list["ReadingBook"]] = relationship("ReadingBook",back_populates="book" )