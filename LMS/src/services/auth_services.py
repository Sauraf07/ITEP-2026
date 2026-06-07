import bcrypt

from src.models.user import User
from src.dao.user_dao import UserDAO


class AuthService:

    @staticmethod
    def register():

        full_name = input("Name : ").strip()

        while True:
            email = input("Email : ").strip()

            if "@" in email and "." in email:
                break

            print("Invalid email format!")

        while True:
            password = input("Password : ")

            if len(password) >= 6:
                break

            print("Password must be at least 6 characters.")

        while True:
            role = input(
                "Role(student/instructor/admin) : "
            ).lower().strip()

            if role in [
                "student",
                "instructor",
                "admin"
            ]:
                break

            print(
                "Invalid role! "
                "Enter student, instructor or admin."
            )

        existing_user = UserDAO.get_by_email(email)

        if existing_user:
            print("Email already registered!")
            return

        password_hash = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

        user = User(
            full_name=full_name,
            email=email,
            password_hash=password_hash,
            role=role
        )

        if UserDAO.save(user):
            print("Registration Successful")
        else:
            print("Registration Failed")

    @staticmethod
    def login():

        email = input("Email : ")
        password = input("Password : ")

        user = UserDAO.get_by_email(email)

        if not user:
            print("User Not Found")
            return None

        if bcrypt.checkpw(
            password.encode(),
            user["password_hash"].encode()
        ):
            print("Login Successful")
            return user

        print("Invalid Password")
        return None