from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base

class Subject(Base):
    __tablename__ = 'subject'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    code:Mapped[int] = mapped_column(Integer)