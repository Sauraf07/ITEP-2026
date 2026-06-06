class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id, enrollment_date):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date

    def __str__(self):
        return (
            f"Enrollment ID: {self.enrollment_id}\n"
            f"Student ID: {self.student_id}\n"
            f"Course ID: {self.course_id}\n"
            f"Date: {self.enrollment_date}"
        )