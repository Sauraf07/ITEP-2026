from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base


class Teacher(Base):
    __tablename__ = 'teacher'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(100))
    phone:Mapped[str] = mapped_column(String(100))
    qualification:Mapped[str] = mapped_column(String(100))
    experience:Mapped[str] = mapped_column(String(100))