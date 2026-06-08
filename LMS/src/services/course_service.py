from src.models.course import Course
from src.dao.course_dao import CourseDAO


class CourseService:

    @staticmethod
    def create_course(instructor_id):

        title = input("Course Title : ")
        description = input("Description : ")

        course = Course(
            title=title,
            description=description,
            instructor_id=instructor_id
        )

        if CourseDAO.save(course):
            print("Course Created Successfully")
        else:
            print("Failed To Create Course")

    @staticmethod
    def view_courses():

        courses = CourseDAO.get_all()

        if not courses:
            print("No Courses Found")
            return

        print("\n===== AVAILABLE COURSES =====")

        for course in courses:

            print(f"""
                        Course ID : {course['course_id']}
                        Title     : {course['title']}
                        Instructor: {course['full_name']}
                        Description:
                        {course['description']}
                        ------------------------------------
                        """)