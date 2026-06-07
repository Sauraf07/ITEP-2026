from src.dao.enrollment_dao import EnrollmentDAO
from src.services.course_service import CourseService


class EnrollmentService:

    @staticmethod
    def enroll_course(student_id):

        CourseService.view_courses()

        course_id = int(
            input("\nEnter Course ID : ")
        )

        if EnrollmentDAO.enroll(
                student_id,
                course_id):

            print("Enrollment Successful")

        else:
            print("Enrollment Failed")

    @staticmethod
    def view_enrolled_courses(student_id):

        courses = EnrollmentDAO.get_student_courses(
            student_id
        )

        if not courses:
            print("No Enrolled Courses")
            return

        print("\n===== MY COURSES =====")

        for course in courses:

            print(f"""
Course ID : {course['course_id']}
Title     : {course['title']}
Description : {course['description']}
----------------------------------
""")
