from src.db_config.database import pool


class CertificateDAO:

    @staticmethod
    def save(
            student_id,
            course_id,
            certificate_path):

        try:

            with pool.get_connection() as conn:
                with conn.cursor() as cursor:

                    sql = "INSERT INTO certificates(student_id,course_id,certificate_path )VALUES (%s,%s,%s) "

                    cursor.execute(
                        sql,
                        (
                            student_id,
                            course_id,
                            certificate_path
                        )
                    )

                    conn.commit()

                    return True

        except Exception as e:
            print(e)
            return False