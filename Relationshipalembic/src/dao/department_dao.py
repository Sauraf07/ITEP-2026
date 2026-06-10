from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import session
from src.db.db_config import  *
from src.model import Department, Employee


class DepartmentDAO:
    @staticmethod
    def fatch_all():
        try:
            with Sessionlocal as session:
                stmt = select(Department)
                result = session.execute(stmt).scalars().all()
                for department in result:
                    print(department.to_dict())
        except SQLAlchemyError as e:
            print(e)

    @staticmethod
    def save_employee(dep_id):
        session = None
        try:
            with Sessionlocal() as session:
                dept = session.get(Department, dep_id)
                if dept:
                    dept.employees.append(Employee(name="Saurav",salary=100000,skills="Python"))
                    dept.employees.append(Employee(name="Sarah",salary=200000,skills="Python"))
                    session.commit()
                    return True
                else:
                    return False
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            print(e)
            return False

    @staticmethod
    def save_department(dept: Department):
        session = None
        try:
            with Sessionlocal() as session:
                session.add(dept)
                session.commit()
                return True

        except SQLAlchemyError as e:
            if session:
                session.rollback()
            print(e)
            return False

