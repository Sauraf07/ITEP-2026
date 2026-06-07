class Result:

    def __init__(
            self,
            result_id=None,
            student_id=None,
            course_id=None,
            score=None,
            total_questions=None):

        self.result_id = result_id
        self.student_id = student_id
        self.course_id = course_id
        self.score = score
        self.total_questions = total_questions