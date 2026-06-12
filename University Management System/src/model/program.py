import integer
from sqlalchemy import create_engine, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship
from src.db.db_config import Base

class Program(Base):
    __tablename__ = 'program'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    degree:Mapped[str] = mapped_column(String(100),nullable=False)
    duration:Mapped[str] = mapped_column(String(100),nullable=False)
    department_id:Mapped[int] = mapped_column(ForeignKey('department.id'))

    department:Mapped["Department"] = relationship("Department", back_populates="program")

    def __repr__(self):
        return "<Program %r>" % self.name

