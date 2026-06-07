class Certificate:

    def __init__(
            self,
            certificate_id=None,
            student_id=None,
            course_id=None,
            certificate_path=None):

        self.certificate_id = certificate_id
        self.student_id = student_id
        self.course_id = course_id
        self.certificate_path = certificate_path