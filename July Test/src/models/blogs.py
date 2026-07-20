from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base


class Blogs(Base):
    __tablename__ = 'blogs'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String(100))
    content:Mapped[str] = mapped_column(String(1000))
    image:Mapped[str] = mapped_column(String(1000))
    create_at:Mapped[DateTime] = mapped_column(DateTime,default=func.now())
    user_id:Mapped[int] = mapped_column(Integer,ForeignKey('user.id'))
    category_id:Mapped[int] = mapped_column(Integer,ForeignKey('categories.id'))
