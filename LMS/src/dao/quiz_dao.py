from src.db_config.database import pool


class QuizDAO:

    @staticmethod
    def save(quiz):

        try:

            with pool.get_connection() as conn:
                with conn.cursor() as cursor:

                    sql = """
                    INSERT INTO quizzes
                    (
                        course_id,
                        title,
                        total_marks
                    )
                    VALUES (%s,%s,%s)
                    """

                    cursor.execute(
                        sql,
                        (
                            quiz.course_id,
                            quiz.title,
                            quiz.total_marks
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

                    cursor.execute(
                        "SELECT * FROM quizzes"
                    )

                    return cursor.fetchall()

        except Exception as e:
            print(e)
            return []