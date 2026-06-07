from src.db_config.database import pool


class UserDAO:

    @staticmethod
    def save(user):

        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:

                    sql = """
                    INSERT INTO users
                    (full_name, email, password_hash, role)
                    VALUES (%s, %s, %s, %s)
                    """

                    cursor.execute(
                        sql,
                        (
                            user.full_name,
                            user.email,
                            user.password_hash,
                            user.role
                        )
                    )

                    conn.commit()
                    return True

        except Exception as e:
            print("Database Error:", e)
            return False

    @staticmethod
    def get_by_email(email):

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

        except Exception as e:
            print("Database Error:", e)
            return None