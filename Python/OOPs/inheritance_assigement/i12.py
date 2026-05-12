'''
12. University System
Person
Student(Person)
GraduateStudent(Student)
Add thesis information.
'''
class Person:
    def role(self):
        print("I am a person")

class Student(Person):
    def role(self):
        print("I am a sudent")

class GraduateStudent(Student):
    def role(self):
        print("I am a graduacte Student")

p = Person()
p.role()
s = Student()
s.role()
g =GraduateStudent()
g.role()