from sqlalchemy import Integer, String, ForeignKey, Column
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base

class ClassRoom(Base):
    __tablename__ = 'classroom'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    clasroom_name:Mapped[String] = mapped_column(String(100))
    room_number:Mapped[int] = mapped_column(Integer)