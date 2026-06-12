from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.db_config import Base
class Student(Base):
    __tablename__ = 'student'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    reg_no:Mapped[str] = mapped_column(String(100),unique=True)
    first_name:Mapped[str] = mapped_column(String(100))
    last_name:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(100),unique=True)
    phone:Mapped[int] = mapped_column(Integer)
    date_of_birth:Mapped[Date] = mapped_column(Date)
    gender:Mapped[str] = mapped_column(String(100))
    admission_date:Mapped[Date] = mapped_column(Date)
    program_id:Mapped[int] = mapped_column(ForeignKey('program.id'))
    advisor_id:Mapped[int] = mapped_column(ForeignKey('advisor.id'))