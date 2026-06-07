class QuizQuestion:

    def __init__(
            self,
            question_id=None,
            quiz_id=None,
            question_text=None,
            option_a=None,
            option_b=None,
            option_c=None,
            option_d=None,
            correct_option=None):

        self.question_id = question_id
        self.quiz_id = quiz_id
        self.question_text = question_text
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.correct_option = correct_option