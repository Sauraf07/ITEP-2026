from src.services.report_service import ReportService


def show_admin_menu(user):

    while True:

        print("\n===== ADMIN MENU =====")
        print("1. Leaderboard")
        print("2. Logout")

        choice = input("Choice : ")

        if choice == "1":
            ReportService.leaderboard()

        elif choice == "2":
            break