class Lesson:
    def __init__(self, lesson_id, course_id, lesson_title, content):
        self.lesson_id = lesson_id
        self.course_id = course_id
        self.lesson_title = lesson_title
        self.content = content

    def __str__(self):
        return (
            f"Lesson ID: {self.lesson_id}\n"
            f"Course ID: {self.course_id}\n"
            f"Title: {self.lesson_title}"
        )