from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db_config import Base
class CourseOffering(Base):
    __tablename__ = 'course_offering'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey('course.id'))
    semester_id: Mapped[int] = mapped_column(ForeignKey('semester.id'))
    section:Mapped[str] = mapped_column(String(10))
    room:Mapped[str] = mapped_column(String(100))
    capacity:Mapped[int] = mapped_column(Integer)
    