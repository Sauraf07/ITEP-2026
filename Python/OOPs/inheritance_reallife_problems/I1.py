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
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @abstractmethod
    def calculate_bonus(self):
        pass

    def display_details(self):
        print("Name :", self.__name)
        print("Salary :", self.__salary)
        print("Bonus :", self.calculate_bonus())

    def get_salary(self):
        return self.__salary

class Developer(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.20

class Manager(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.35

class Intern(Employee):

    def calculate_bonus(self):
        return 5000

d1 = Developer("Saurav", 50000)
m1 = Manager("Rohit", 80000)
i1 = Intern("Ankit", 20000)

d1.display_details()
print("="*20)
m1.display_details()
print("="*20)
i1.display_details()
