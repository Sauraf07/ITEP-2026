'''
1. Employee Bonus Calculator
Problem Statement
A company gives bonuses differently based on employee type.
Create:
abstract class Employee
child classes:
Developer
Manager
Intern
Rules:
Developer → 20% bonus
Manager → 35% bonus
Intern → fixed ₹5000 bonus
Requirements
Methods:
calculate_bonus()
display_details()
Concepts
Abstract class
Method overriding
Business logic
'''
from abc import *
class Employee(ABC):
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    @abstractmethod
    def calculate_bonous(self):
        pass
    @abstractmethod
    def display_details(self):
        print(f"Name : {self.__name}")
        print(f"Salary : {self.__salary}")
        print(f"bonous : {self.calculate_bonous()}")

    def get_name(self):
        return self.__name

    def  get_salary(self):
        return self.__name


class Developer(Employee):
    salary = 5000
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonous(self,bonous):
        self.__bonous = bonous
        self.salary = self.salary + ((self.salary*self.__bonous)/100)

    def display_details(self):
        return super().display_details()   
        
    def get_bonous(self):
        return self.__bonous

class Manager(Employee):
    pass

class Intern(Employee):
    pass

d1 = Developer("Saurav",5000)
d1.display_details()
d1.calculate_bonous(20)
