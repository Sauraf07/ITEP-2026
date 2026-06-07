from src.services.course_service import CourseService
from src.services.enrollment_service import EnrollmentService
from src.services.lesson_service import LessonService
from src.services.quiz_service import QuizService
from src.services.report_service import ReportService
from src.services.certificate_service import CertificateService


def show_student_menu(user):

    while True:

        print("\n===== Student Menu =====")
        print("1. View Courses")
        print("2. Enroll Course")
        print("3. My Courses")
        print("4. View Lessons")
        print("5. Attempt Quiz")
        print("6. My Results")
        print("7. Generate Certificate")
        print("8. Logout")

        choice = input("Enter Choice : ")

        if choice == "1":
            CourseService.view_courses()

        elif choice == "2":
            EnrollmentService.enroll_course(
                user["user_id"]
            )

        elif choice == "3":
            EnrollmentService.view_enrolled_courses(
                user["user_id"]
            )

        elif choice == "4":
            LessonService.view_lessons()


        elif choice == "5":

            QuizService.attempt_quiz(

                user["user_id"]

            )


        elif choice == "6":

            ReportService.student_report(

                user["user_id"]

            )



        elif choice == "7":

            CertificateService.generate_certificate()


        elif choice == "8":

            break