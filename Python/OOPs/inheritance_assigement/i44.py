'''
44. Online Examination System
Features:
Student
Exam
Result
Use abstract classes for exams.
'''
from abc import ABC, abstractmethod
class Exam(ABC):

    @abstractmethod
    def conduct_exam(self):
        pass

class Student(Exam):

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def conduct_exam(self):
        print(f"Exam conducted for {self.name}")

class Result:

    def show_result(self, student):
        if student.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

s = Student("Saurav", 75)
s.conduct_exam()
r = Result()
r.show_result(s)