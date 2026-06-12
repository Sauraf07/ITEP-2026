from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db_config import Base
class Semester(Base):
    __tablename__ = 'semester'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    start_date:Mapped[Date] = mapped_column(Date,nullable=False)
    end_date:Mapped[Date] = mapped_column(Date,nullable=False)
    academic_year:Mapped[str] = mapped_column(String,nullable=False)
    