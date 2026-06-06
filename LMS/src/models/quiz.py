class Quiz:
    def __init__(
        self,
        quiz_id,
        course_id,
        question,
        option1,
        option2,
        option3,
        option4,
        correct_option
    ):
        self.quiz_id = quiz_id
        self.course_id = course_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correct_option = correct_option

    def __str__(self):
        return (
            f"Quiz ID: {self.quiz_id}\n"
            f"Question: {self.question}"
        )