from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapper, mapped_column, Mapped

from src.db.db_config import Base
class Course(Base):
    __tablename__ = 'courses'
    id:Mapped[int] = mapped_column(Integer,1,primary_key=True)
    course_code:Mapped[str] = mapped_column(String(100),unique=True)
    course_title:Mapped[int] = mapped_column(String(100))
    course_hours:Mapped[int] = mapped_column(Integer)
    department_id:Mapped[int] = mapped_column(ForeignKey('department.id'))
    
