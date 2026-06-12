from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.db_config import Base
class Payment(Base):
    __tablename__ = 'payment'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    student_id:Mapped[int] = mapped_column(ForeignKey('student.id'))
    amount:Mapped[int] = mapped_column(Integer)
    