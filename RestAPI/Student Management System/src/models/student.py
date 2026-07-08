from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base
class Student(Base):
    __tablename__ = 'student'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(100))
    course:Mapped[str] = mapped_column(String(100))
    age:Mapped[int] = mapped_column(Integer)