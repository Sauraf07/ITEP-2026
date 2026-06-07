from src.db_config.database import pool


class EnrollmentDAO:

    @staticmethod
    def enroll(student_id, course_id):

        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:

                    sql = """
                    INSERT INTO enrollments
                    (student_id, course_id)
                    VALUES (%s, %s)
                    """

                    cursor.execute(
                        sql,
                        (student_id, course_id)
                    )

                    conn.commit()
                    return True

        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_student_courses(student_id):

        try:
            with pool.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:

                    sql = """
                    SELECT
                        c.course_id,
                        c.title,
                        c.description
                    FROM enrollments e
                    JOIN courses c
                    ON e.course_id = c.course_id
                    WHERE e.student_id = %s
                    """

                    cursor.execute(sql, (student_id,))

                    return cursor.fetchall()

        except Exception as e:
            print(e)
            return []