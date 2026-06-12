from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.db_config import Base
class GradeScale(Base):
    __tablename__ = 'grade_scale'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    min_marks:Mapped[int] = mapped_column(Integer)
    max_marks:Mapped[int] = mapped_column(Integer)
    grade_point:Mapped[float] = mapped_column(Integer)