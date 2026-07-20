from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column

from src.db.db_config import Base
class Comment(Base):
    __tablename__ = 'comment'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    comment:Mapped[str] = mapped_column(String(100))
    create_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    user_id:Mapped[int] = mapped_column(Integer,ForeignKey('user.id'))
    blog_id:Mapped[int] = mapped_column(Integer,ForeignKey('blogs.id'))
