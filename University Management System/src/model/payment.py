from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.db_config import Base
class Payment(Base):
    __tablename__ = 'payment'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    student_id:Mapped[int] = mapped_column(ForeignKey('student.id'))
    payment_date:Mapped[Date] = mapped_column(Date)
    amount:Mapped[int] = mapped_column(Integer)
    payment_type:Mapped[str] = mapped_column(String(20))
    reference_no:Mapped[str] = mapped_column(String(50))