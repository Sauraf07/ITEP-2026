from src.db_config.database import pool


class QuizQuestionDAO:

    @staticmethod
    def save(question):

        try:

            with pool.get_connection() as conn:
                with conn.cursor() as cursor:

                    sql = """
                    INSERT INTO quiz_questions
                    (
                        quiz_id,
                        question_text,
                        option_a,
                        option_b,
                        option_c,
                        option_d,
                        correct_option
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                    """

                    cursor.execute(
                        sql,
                        (
                            question.quiz_id,
                            question.question_text,
                            question.option_a,
                            question.option_b,
                            question.option_c,
                            question.option_d,
                            question.correct_option
                        )
                    )

                    conn.commit()

                    return True

        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_questions_by_quiz(quiz_id):

        try:
            with pool.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:
                    sql = """
                          SELECT *
                          FROM quiz_questions
                          WHERE quiz_id = %s \
                          """

                    cursor.execute(sql, (quiz_id,))

                    return cursor.fetchall()

        except Exception as e:
            print(e)
            return []