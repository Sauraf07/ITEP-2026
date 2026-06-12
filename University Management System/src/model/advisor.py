from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.db_config import Base
class Advisor(Base):
    __tablename__ = 'advisor'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    teacher_id:Mapped[int] = mapped_column(ForeignKey('teacher.id'))
    student_id:Mapped[int] = mapped_column(ForeignKey('student.id'))
    advisor_date:Mapped[Date] = mapped_column(Date)