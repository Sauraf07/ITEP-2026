from src.models.lesson import Lesson
from src.dao.lesson_dao import LessonDAO
from src.services.course_service import CourseService


class LessonService:

    @staticmethod
    def add_lesson():

        CourseService.view_courses()

        course_id = int(
            input("\nCourse ID : ")
        )

        lesson_title = input(
            "Lesson Title : "
        )

        content = input(
            "Lesson Content : "
        )

        lesson_content = input("Lesson Content : ")
        lesson_order = int(input("Lesson Order : "))

        lesson = Lesson(
            course_id=course_id,
            lesson_title=lesson_title,
            lesson_content=lesson_content,
            lesson_order=lesson_order
        )

        if LessonDAO.save(lesson):
            print("Lesson Added Successfully")
        else:
            print("Failed To Add Lesson")

    @staticmethod
    def view_lessons():

        CourseService.view_courses()

        course_id = int(
            input("\nCourse ID : ")
        )

        lessons = LessonDAO.get_by_course(
            course_id
        )

        if not lessons:
            print("No Lessons Found")
            return

        print("\n===== LESSONS =====")

        for lesson in lessons:
            print(f"""
            Lesson ID : {lesson['lesson_id']}
            Title     : {lesson['lesson_title']}
            Order     : {lesson['lesson_order']}

            Content:
            {lesson['lesson_content']}
            -------------------------------------
            """)