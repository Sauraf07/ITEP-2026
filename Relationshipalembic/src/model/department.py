from ast import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship,mapped_column,Mapped

from src.db.db_config import Base


class Department(Base):
    __tablename__ = 'department'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    code:Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    employee:Mapped[list["Employee"]] = relationship("Employee", back_populates="department",cascade="all,delete-orphan")


    def __repr__(self):
        return f"<Department {self.id} {self.name} {self.code} {self.employee}> "