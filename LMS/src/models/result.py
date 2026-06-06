class Result:
    def __init__(self, result_id, student_id, course_id, score):
        self.result_id = result_id
        self.student_id = student_id
        self.course_id = course_id
        self.score = score

    def __str__(self):
        return (
            f"Result ID: {self.result_id}\n"
            f"Student ID: {self.student_id}\n"
            f"Course ID: {self.course_id}\n"
            f"Score: {self.score}"
        )