from src.db_config.database import pool


class CourseDAO:

    @staticmethod
    def save(course):

        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:

                    sql = """
                    INSERT INTO courses
                    (title, description, instructor_id)
                    VALUES (%s, %s, %s)
                    """

                    cursor.execute(
                        sql,
                        (
                            course.title,
                            course.description,
                            course.instructor_id
                        )
                    )

                    conn.commit()
                    return True

        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_all():

        try:
            with pool.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:

                    sql = """SELECT c.course_id,c.title,c.description,u.full_name FROM courses c JOIN users u ON c.instructor_id = u.user_id
                    """

                    cursor.execute(sql)

                    return cursor.fetchall()

        except Exception as e:
            print(e)
            return []