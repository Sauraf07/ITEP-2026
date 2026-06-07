from src.dao.report_dao import ReportDAO


class ReportService:

    @staticmethod
    def student_report(student_id):

        results = ReportDAO.get_student_results(student_id)

        if not results:
            print("No Quiz History Found")
            return

        print("\n===== MY RESULTS =====")

        for result in results:

            print(f"""
                        Course : {result['title']}
                        Score  : {result['score']}
                        Total  : {result['total_questions']}
                        Date   : {result['attempted_at']}
                        ---------------------------------
                        """)

    @staticmethod
    def leaderboard():

        data = ReportDAO.get_leaderboard()

        if not data:
            print("No Data Found")
            return

        print("\n===== LEADERBOARD =====")

        rank = 1

        for row in data:

            print(f"{rank}. " f"{row['full_name']} " f"({row['total_score']} pts)")

            rank += 1
