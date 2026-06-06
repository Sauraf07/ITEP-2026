class Course:
    def __init__(self, course_id, title, description, instructor_id):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.instructor_id = instructor_id

    def __str__(self):
        return (
            f"Course ID: {self.course_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Instructor ID: {self.instructor_id}"
        )