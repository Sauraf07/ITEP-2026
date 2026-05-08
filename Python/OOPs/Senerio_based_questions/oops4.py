'''
4. Student Grade System
Problem
Create a student result management system.
Requirements
Each student should have:
roll number
name
marks in 3 subjects
Functionalities
Calculate total marks
Calculate percentage
Assign grade:
A → 90+
B → 75+
C → 50+
Fail otherwise
Track total students
Concepts Practiced
instance methods
conditional logic in classes
object-based calculations
'''
class Student:
    total_students = 0
    def __init__(self, roll_num, name, marks):
        self.__roll_num = roll_num
        self.__name = name
        self.__marks = marks
        Student.total_students += 1
    
    def total_marks(self):
        return sum(self.__marks)
    
    def percentage(self):
        return self.total_marks() / len(self.__marks)
    
    def Details(self):
        print(f"Name : {self.__name}")
        print(f"Rollno. {self.__roll_num}")
        print(f"Makrs : {self.__marks}")
    
    def grade(self):
        percent = self.percentage()
        if percent >= 90:
            return 'A'
        elif percent >= 75:
            return 'B'
        elif percent >= 50:
            return 'C'
        else:
            return 'Fail'
    
    @classmethod
    def total_students_count(cls):
        return cls.total_students
    
student1 = Student(1, "Cheeku", [85, 92, 78])
print(f"Total Marks: {student1.total_marks()}")
print(f"Percentage: {student1.percentage() }%")
print(f"Grade: {student1.grade()}")
student1.Details()

  

         

    