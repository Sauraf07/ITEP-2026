from src.db_config.database import pool


class LessonDAO:

    @staticmethod
    def save(lesson):

        try:

            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = """
                          INSERT INTO lessons
                          (course_id, \
                           lesson_title, \
                           lesson_content, \
                           lesson_order)
                          VALUES (%s, %s, %s, %s) \
                          """

                    cursor.execute(
                        sql,
                        (
                            lesson.course_id,
                            lesson.lesson_title,
                            lesson.lesson_content,
                            lesson.lesson_order
                        )
                    )

                    conn.commit()

                    return True

        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_by_course(course_id):

        try:
            with pool.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:

                    sql = """
                    SELECT *
                    FROM lessons
                    WHERE course_id=%s
                    """

                    cursor.execute(sql, (course_id,))
                    return cursor.fetchall()

        except Exception as e:
            print(e)
            return []