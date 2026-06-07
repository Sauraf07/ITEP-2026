class Lesson:

    def __init__(
            self,
            lesson_id=None,
            course_id=None,
            lesson_title=None,
            lesson_content=None,
            lesson_order=None):

        self.lesson_id = lesson_id
        self.course_id = course_id
        self.lesson_title = lesson_title
        self.lesson_content = lesson_content
        self.lesson_order = lesson_order