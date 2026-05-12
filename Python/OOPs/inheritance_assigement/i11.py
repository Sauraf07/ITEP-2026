'''
11. Company Hierarchy
Person
Employee(Person)
Manager(Employee
Display company hierarchy.
'''
class Person:
    def role(self):
        print("I am a Person")

class Employee(Person):
    def role(self):
        print("I am a Employee")

class Manager(Employee):
    def role(self):
        print("I am a  manager")
p = Person()
p.role()
e = Employee()
e.role()
m = Manager()
m.role()