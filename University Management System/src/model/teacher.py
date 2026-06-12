from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.db_config import Base
class Teacher(Base):
    __tablename__ = 'teacher'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    employee_no:Mapped[str] = mapped_column(String,unique=True)
    first_name:Mapped[str] = mapped_column(String(100))
    last_name:Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    phone: Mapped[int] = mapped_column(Integer)
    hire_date:Mapped[Date] = mapped_column(Date)
    department:Mapped[str] = mapped_column(ForeignKey('department.department_id'))
