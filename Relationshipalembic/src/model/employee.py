from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship

from src.model import Department


class Employee(Department):
    __tablename__ = 'employee'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    salary:Mapped[int] = mapped_column(Integer,nullable=False)
    skills:Mapped[str] = mapped_column(String(100),nullable=False)

    department_id:Mapped[int] = mapped_column(ForeignKey("department.id"))

    department:Mapped["Department"] = relationship("Department",back_populates="employees")

    def __repr__(self):
        return f"{self.id} {self.name} {self.salary} {self.skills} {self.department_id}"
