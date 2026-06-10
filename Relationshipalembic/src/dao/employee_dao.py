from select import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_serializer import SerializerMixin

from src.db.db_config import Sessionlocal
from src.model import Employee


class EmployeeDAO:
    @staticmethod
    def fetch_by_skills(skill):
        try:
            with Sessionlocal() as session:
                stmt = select(Employee).where(Employee.skill ==skill)
                result = session.execute(stmt).scalar().all()
                result = [employee.to_dict() for employee in result]
                print(result)
        except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def fetch_all():
        try:
            with Sessionlocal() as session
                stmt = select(Employee)

        except SQLAlchemyError as e:
            print(e)