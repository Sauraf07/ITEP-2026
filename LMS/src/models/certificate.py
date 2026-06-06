class Certificate:
    def __init__(
        self,
        certificate_id,
        student_id,
        course_id,
        issue_date
    ):
        self.certificate_id = certificate_id
        self.student_id = student_id
        self.course_id = course_id
        self.issue_date = issue_date

    def __str__(self):
        return (
            f"Certificate ID: {self.certificate_id}\n"
            f"Student ID: {self.student_id}\n"
            f"Course ID: {self.course_id}\n"
            f"Issue Date: {self.issue_date}"
        )