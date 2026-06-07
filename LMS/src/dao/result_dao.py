from src.db_config.database import pool


class ResultDAO:

    @staticmethod
    def save_result(
            student_id,
            course_id,
            score,
            total_questions):

        try:

            with pool.get_connection() as conn:
                with conn.cursor() as cursor:

                    sql = """
                    INSERT INTO results
                    (
                        student_id,
                        course_id,
                        score,
                        total_questions
                    )
                    VALUES (%s,%s,%s,%s)
                    """

                    cursor.execute(
                        sql,
                        (
                            student_id,
                            course_id,
                            score,
                            total_questions
                        )
                    )

                    conn.commit()

                    return True

        except Exception as e:
            print(e)
            return False