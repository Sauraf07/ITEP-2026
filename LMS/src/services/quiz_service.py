from src.models.quiz import Quiz
from src.models.quiz_question import QuizQuestion
from src.dao.quiz_dao import QuizDAO
from src.dao.quiz_question_dao import QuizQuestionDAO
from src.dao.result_dao import ResultDAO
from src.services.course_service import CourseService


class QuizService:

    @staticmethod
    def create_quiz():

        CourseService.view_courses()

        course_id = int(input("\nCourse ID : "))

        title = input("Quiz Title : ")

        total_marks = int(
            input("Total Marks : ")
        )

        quiz = Quiz(
            course_id=course_id,
            title=title,
            total_marks=total_marks
        )

        if QuizDAO.save(quiz):
            print("Quiz Created Successfully")
        else:
            print("Failed To Create Quiz")

    @staticmethod
    def add_question():

        quizzes = QuizDAO.get_all()

        print("\n===== QUIZZES =====")

        for quiz in quizzes:

            print(
                f"{quiz['quiz_id']} - {quiz['title']}"
            )

        quiz_id = int(
            input("\nQuiz ID : ")
        )

        question_text = input(
            "Question : "
        )

        option_a = input("Option A : ")
        option_b = input("Option B : ")
        option_c = input("Option C : ")
        option_d = input("Option D : ")

        correct_option = input(
            "Correct Option (A/B/C/D): "
        ).upper()

        question = QuizQuestion(
            quiz_id=quiz_id,
            question_text=question_text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_option=correct_option
        )

        if QuizQuestionDAO.save(question):
            print("Question Added Successfully")
        else:
            print("Failed To Add Question")

    @staticmethod
    def attempt_quiz(student_id):

        quizzes = QuizDAO.get_all()

        if not quizzes:
            print("No Quizzes Available")
            return

        print("\n===== AVAILABLE QUIZZES =====")

        for quiz in quizzes:
            print(
                f"{quiz['quiz_id']} - "
                f"{quiz['title']}"
            )

        quiz_id = int(
            input("\nQuiz ID : ")
        )

        selected_quiz = None

        for quiz in quizzes:

            if quiz["quiz_id"] == quiz_id:
                selected_quiz = quiz
                break

        if not selected_quiz:
            print("Invalid Quiz ID")
            return

        questions = (
            QuizQuestionDAO
            .get_questions_by_quiz(quiz_id)
        )

        if not questions:
            print("No Questions Found")
            return

        score = 0

        print("\n===== QUIZ STARTED =====")

        for q in questions:

            print("\n")
            print(q["question_text"])

            print("A.", q["option_a"])
            print("B.", q["option_b"])
            print("C.", q["option_c"])
            print("D.", q["option_d"])

            answer = input(
                "Your Answer : "
            ).upper()

            if answer == q["correct_option"]:
                score += 1

        total_questions = len(questions)

        ResultDAO.save_result(
            student_id,
            selected_quiz["course_id"],
            score,
            total_questions
        )

        print("\n===== RESULT =====")

        print(
            f"Score : "
            f"{score}/{total_questions}"
        )