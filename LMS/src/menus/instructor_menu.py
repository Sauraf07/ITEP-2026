from src.services.course_service import CourseService
from src.services.lesson_service import LessonService
from src.services.quiz_service import QuizService


def show_instructor_menu(user):

    while True:

        print("\n===== Instructor Menu =====")
        print("1. Create Course")
        print("2. View Courses")
        print("3. Add Lesson")
        print("4. View Lessons")
        print("5. Create Quiz")
        print("6. Add Quiz Question")
        print("7. Logout")


        choice = input("Enter Choice : ")

        if choice == "1":
            CourseService.create_course(
                user["user_id"]
            )

        elif choice == "2":
            CourseService.view_courses()

        elif choice == "3":
            LessonService.add_lesson()

        elif choice == "4":
            LessonService.view_lessons()

        elif choice == "5":

            QuizService.create_quiz()

        elif choice == "6":

            QuizService.add_question()

        elif choice == "7":

             break

