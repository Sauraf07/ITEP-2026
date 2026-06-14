from sqlalchemy.exc import SQLAlchemyError

from src.db.db_config import SessionLocal
from src.model.user import User


class UserDAO:

    @staticmethod
    def save(user: User):
        try:
            with SessionLocal() as session:
                session.add(user)
                session.commit()
                session.refresh(user)
                return user

        except SQLAlchemyError as e:
            print(e)
            return None

    @staticmethod
    def fetch_by_id(user_id):
        try:
            with SessionLocal() as session:
                return session.get(User, user_id)

        except SQLAlchemyError as e:
            print(e)
            return None

    @staticmethod
    def fetch_all():
        try:
            with SessionLocal() as session:
                return session.query(User).all()

        except SQLAlchemyError as e:
            print(e)
            return []

    @staticmethod
    def update(user: User):
        try:
            with SessionLocal() as session:

                db_user = session.get(User, user.id)

                if db_user:
                    db_user.name = user.name
                    db_user.email = user.email
                    db_user.password = user.password
                    db_user.phone = user.phone
                    db_user.role = user.role
                    db_user.updated_at = user.updated_at

                    session.commit()
                    return True

                return False

        except SQLAlchemyError as e:
            print(e)
            return False

    @staticmethod
    def delete(user_id):
        try:
            with SessionLocal() as session:

                user = session.get(User, user_id)

                if user:
                    session.delete(user)
                    session.commit()
                    return True

                return False

        except SQLAlchemyError as e:
            print(e)
            return False