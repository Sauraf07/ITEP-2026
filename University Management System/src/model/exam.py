from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.db_config import Base

class Exam(Base):
    __tablename__ = 'exam'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    offering_id:Mapped[int] = mapped_column(ForeignKey('course_offering.id'))
    exam_type:Mapped[str] = mapped_column(String(50))
    exam_date:Mapped[Date] = mapped_column(Date)
    max_marks:Mapped[int] = mapped_column(Integer)