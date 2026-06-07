from src.db_config.database import pool


class ReportDAO:

    @staticmethod
    def get_student_results(student_id):

        try:
            with pool.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:

                    sql = """
                    SELECT
                        c.title,
                        r.score,
                        r.total_questions,
                        r.attempted_at
                    FROM results r
                    JOIN courses c
                    ON r.course_id = c.course_id
                    WHERE r.student_id=%s
                    ORDER BY r.attempted_at DESC
                    """

                    cursor.execute(
                        sql,
                        (student_id,)
                    )

                    return cursor.fetchall()

        except Exception as e:
            print(e)
            return []

    @staticmethod
    def get_leaderboard():

        try:
            with pool.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:

                    sql = """
                    SELECT
                        u.full_name,
                        SUM(r.score) AS total_score
                    FROM users u
                    JOIN results r
                    ON u.user_id = r.student_id
                    GROUP BY u.user_id
                    ORDER BY total_score DESC
                    """

                    cursor.execute(sql)

                    return cursor.fetchall()

        except Exception as e:
            print(e)
            return []