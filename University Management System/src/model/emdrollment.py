from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.db_config import Base
class Endrollment(Base):
    __tablename__ = 'enrollment'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    student_id:Mapped[int] = mapped_column(ForeignKey('student.id'))
    offering_id:Mapped[int] = mapped_column(ForeignKey('course_offering.id'))
    enrolment_date:Date = mapped_column(Date)
    status:Mapped[str] = mapped_column(String)
    final_grade:Mapped[str] = mapped_column(String)