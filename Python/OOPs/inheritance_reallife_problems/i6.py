'''
6. Exam Evaluation System
Problem Statement
Marks are evaluated differently.
Create:
abstract class Exam
Child:
MCQExam
PracticalExam
VivaExam
Each calculates grades differently.
'''
from abc import *
class Exam(ABC):
    def __init__(self,marks):
        self.__marks = marks
    
    @abstractmethod
    def total_grade(self):
        pass
    def get_marks(self):
        return self.__marks

class MCQExam(Exam):
    def total_grade(self):
        print(f"Your Total Marks in MCQ EXAM is  {self.get_marks()} ")
        if self.get_marks() > 90:
            print("Your got A grade")
        elif self.get_marks() > 60:
            print("You Get B Grade")
        elif self.get_marks() > 45:
            print("You Get C grade ")
        else: print("You fail ")

class PracticalExam(Exam):
    def total_grade(self):
        print(f"You Got marks in Practical Exam {self.get_marks()}")
        if self.get_marks() > 50:
            print("You pass ")
        else:
            print("You fail")

class VivaExam(Exam):
    def total_grade(self):
        print(f" Your total marks in Viva Exam is {self.get_marks()}")
        if self.get_marks() > 70:
            print(f"You pass the viva exam with good marks. !Well Done ")
        elif self.get_marks() > 50:
            print("You the viva exam but with average numbers. !Work Hard ")
        else:
            print("You fail The Viva Exam. !Better luck next time ")

e1 = MCQExam(91)
e1.total_grade()
print("="*20)
e2 = PracticalExam(66)
e2.total_grade()
print("="*20)
e3 = VivaExam(45)
e3.total_grade()