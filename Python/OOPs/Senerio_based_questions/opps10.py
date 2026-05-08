'''
10. Company Department System
Problem

Create:

Department
Employee

classes.

Requirements

Each department:

has department name
stores employee objects
Functionalities
Add employee to department
Display all employees
Calculate total department salary
Concepts Practiced
object composition
object interaction
storing objects in lists
Department :-
  property : name, employee_list
  behaviour: add_employee(employee_object),display(),total_department_salary()
Employee :-
  property : id,name,salary
'''
class Department:
    def __init__(self,name):
        self.__name = name
        self.__employee = []

    def add_employee(self,a):
        self.__employee.append(a)

    def display(self):
        for emp in self.__employee:
            print(emp)

class Employee:
    def __init__(self,id,name,salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def __str__(self):
        return str(self.__id) + " : "+self.__name+" : "+ str(self.__salary)
        
d1 = Department("IT")
d2 = Department("sales")

e1 = Employee(101,"Saurav",10000)
e2 = Employee(102,"Gaurav",1000)

d1.add_employee(e1)
d2.add_employee(e2)

d1.display()
print("="*50)
d2.display()

        