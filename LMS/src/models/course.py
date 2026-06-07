class Course:

    def __init__(
            self,
            course_id=None,
            title=None,
            description=None,
            instructor_id=None):

        self.course_id = course_id
        self.title = title
        self.description = description
        self.instructor_id = instructor_id