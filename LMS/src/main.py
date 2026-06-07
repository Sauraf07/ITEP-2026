from src.services.auth_services import AuthService
from src.menus.admin_menu import show_admin_menu
from src.menus.instructor_menu import show_instructor_menu
from src.menus.student_menu import show_student_menu


while True:

    print("\n===== LearnTrack LMS =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        AuthService.register()

    elif choice == "2":

        user = AuthService.login()

        if not user:
            print("Invalid Credentials")
            continue

        role = user["role"]

        if role == "admin":
            show_admin_menu(user)

        elif role == "instructor":
            show_instructor_menu(user)

        elif role == "student":
            show_student_menu(user)

    elif choice == "3":
        print("Thank You For Using LearnTrack LMS")
        break

    else:
        print("Invalid Choice")