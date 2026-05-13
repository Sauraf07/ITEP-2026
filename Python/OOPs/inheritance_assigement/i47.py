'''
47. School ERP System

Features:

attendance
exams
student records
teacher management
'''
from abc import *
class School(ABC):  
    @abstractmethod
    def attendance(self):
        pass
    @abstractmethod
    def exams(self):
        pass
    @abstractmethod
    def studentrecords(self):
        pass
    @abstractmethod
    def teachermanagement(self):
        pass
class ABCSchool(School):
    def attendance(self):
        print("Attendance marked")

    def exams(self):
        print("Exams scheduled")

    def studentrecords(self):
        print("Student records maintained")

    def teachermanagement(self):
        print("Teacher management system in place")
s1 = ABCSchool()
s1.attendance()
s1.exams()
s1.studentrecords()
s1.teachermanagement()
