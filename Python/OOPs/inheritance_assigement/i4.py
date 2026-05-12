'''4. Student Management
Base class Person.
Derived:
Student
Teacher
Add role-specific methods
'''
class Person:
    def role(self):
        pass
class Student(Person):
    def role(self):
        print("I am a student")

class Teacher(Person):
    def role(self):
        print("I am a Teacher")

s = Student()
s.role()
t = Teacher()
t.role()