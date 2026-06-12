from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base
class Department(Base):
    __tablename__ = 'department'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String)
    office_location:Mapped[str] = mapped_column(String)
    phone_number:Mapped[str] = mapped_column(String)
    email:Mapped[str] = mapped_column(String)