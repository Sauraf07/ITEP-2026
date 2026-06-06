from services.auth_service import register, login
from course import create_course, view_courses, enroll_course


while True:

    print("\n===== LearnTrack LMS =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register()

    elif choice == "2":

        user = login()

        if user:

            user_id = user[0]
            role = user[4]

            print("Login Successful!")

            if role == "instructor":

                while True:

                    print("\nInstructor Menu")
                    print("1. Create Course")
                    print("2. View Courses")
                    print("3. Logout")

                    ch = input("Choice: ")

                    if ch == "1":
                        create_course(user_id)

                    elif ch == "2":
                        view_courses()

                    elif ch == "3":
                        break

            elif role == "student":

                while True:

                    print("\nStudent Menu")
                    print("1. View Courses")
                    print("2. Enroll Course")
                    print("3. Logout")

                    ch = input("Choice: ")

                    if ch == "1":
                        view_courses()

                    elif ch == "2":
                        enroll_course(user_id)

                    elif ch == "3":
                        break

        else:
            print("Invalid Credentials")

    elif choice == "3":
        print("Goodbye!")
        break