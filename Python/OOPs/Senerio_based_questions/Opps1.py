'''
1. Employee Management System
Problem
Create an Employee class to manage employee details.
Requirements
Each employee should have:
employee id
name
department
salary
Functionalities
Display employee details
Increase salary by percentage
Count total employees created using a class variable
Create employee object from a string:
"101-Rahul-IT-50000"
using a class method.
Concepts Practiced
constructor
instance variables
class variables
class method
instance methods
'''
class Employee:
    count = 0
    def __init__(self,emp_id,name,dep,salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__dep = dep
        self.__salary = salary
        Employee.count += 1
    
    @classmethod
    def Count_employees(cls):
        return cls.count
    
    def emp_details(self):
        print(f"Id : {self.__emp_id}")
        print(f"Name : {self.__name}")
        print(f"Department : {self.__dep}")
        print(f"Salary : {self.__salary}")

    def increase_salary(self, percentage):
        self.__salary += self.__salary * (percentage / 100)

    @classmethod
    def from_string(cls,emp_str):
        emp_id, name, dep, salary = emp_str.split('-')
        return cls(emp_id, name, dep, float(salary))
    
emp1 = Employee.from_string("101-Rahul-IT-50000")
emp1.increase_salary(5)
emp1.emp_details()
em2 = Employee.from_string("102-Saurav-CS-1000")
em2.emp_details()
print(f"Total Employees: {Employee.Count_employees()}")
        