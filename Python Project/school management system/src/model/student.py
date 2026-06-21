from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base
class Student(Base):
    __tablename__ = 'student'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    age:Mapped[int] = mapped_column(Integer,nullable=False)
    gender:Mapped[int] = mapped_column(Integer,nullable=False)
    email:Mapped[str] = mapped_column(String(100),nullable=False)
    phone:Mapped[int] = mapped_column(Integer,nullable=False)
    classroom_id:Mapped[int] = mapped_column(ForeignKey('classroom.id'),nullable=False)

