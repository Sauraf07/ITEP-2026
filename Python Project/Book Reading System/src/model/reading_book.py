import datetime

from sqlalchemy import Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base
class ReadingBook(Base):
    __tablename__ = "reading_book"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    pages_read:Mapped[int] = mapped_column(Integer)
    reading_date:Mapped[Date] = mapped_column(Date,default=datetime.date.today)
    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"),nullable=False)
    book: Mapped["Book"] = relationship("Book",back_populates="reading_sessions")

    
