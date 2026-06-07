class Quiz:

    def __init__(
            self,
            quiz_id=None,
            course_id=None,
            title=None,
            total_marks=None):

        self.quiz_id = quiz_id
        self.course_id = course_id
        self.title = title
        self.total_marks = total_marks