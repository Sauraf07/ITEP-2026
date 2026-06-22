from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column
from src.db.db_config import Base
class Post(Base):
    __tablename__ = 'post'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String(200),nullable=False)
    content:Mapped[str] = mapped_column(String(1000),nullable=False)
    user_id:Mapped[int] = mapped_column(ForeignKey('user.id'))