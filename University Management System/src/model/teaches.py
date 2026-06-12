from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.db_config import Base
class Teaches(Base):
    __tablename__ = 'teaches'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    teacher_id:Mapped[int] = mapped_column(ForeignKey('teacher.id'))
    offering_id:Mapped[int] = mapped_column(ForeignKey('course_offering.id'))
    role:Mapped[str] = mapped_column(String(50))