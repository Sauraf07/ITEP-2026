from mysql.connector import Error
from db_config.database import pool
import bcrypt


class AuthService:

    @staticmethod
    def register(name, email, password, role):
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:

                    hashed_password = bcrypt.hashpw(
                        password.encode(),
                        bcrypt.gensalt()
                    ).decode()

                    sql = """
                    INSERT INTO users(name,email,password,role)
                    VALUES(%s,%s,%s,%s)
                    """

                    cursor.execute(
                        sql,
                        (name, email, hashed_password, role)
                    )

                    conn.commit()
                    return True

        except Error as e:
            print(e)

            if conn and conn.is_connected():
                conn.rollback()

            return False

    @staticmethod
    def login(email, password):
        try:
            with pool.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:

                    sql = """
                    SELECT * FROM users
                    WHERE email = %s
                    """

                    cursor.execute(sql, (email,))

                    user = cursor.fetchone()

                    if user:

                        if bcrypt.checkpw(
                            password.encode(),
                            user["password"].encode()
                        ):
                            return user

                    return None

        except Error as e:
            print(e)
            return None

    @staticmethod
    def fetch_all_users():
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:

                    sql = """
                    SELECT user_id,name,email,role
                    FROM users
                    """

                    cursor.execute(sql)

                    rows = cursor.fetchall()

                    for row in rows:
                        user_id, name, email, role = row

                        print(
                            f"{user_id} : {name} : {email} : {role}"
                        )

        except Error as e:
            print(e)

    @staticmethod
    def delete_user(user_id):
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:

                    sql = """
                    DELETE FROM users
                    WHERE user_id = %s
                    """

                    cursor.execute(sql, (user_id,))

                    conn.commit()

                    return cursor.rowcount > 0

        except Error as e:

            if conn and conn.is_connected():
                conn.rollback()

            print(e)
            return False

    @staticmethod
    def find_by_email(email):
        try:
            with pool.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:

                    sql = """
                    SELECT *
                    FROM users
                    WHERE email = %s
                    """

                    cursor.execute(sql, (email,))

                    return cursor.fetchone()

        except Error as e:
            print(e)
            return None