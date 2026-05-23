'''Question 1 — Inheritance and Method Overriding

Create a class Employee with the following:

Instance variables:
name
salary
Method:
display_details()

Create a child class Manager that inherits from Employee.

Additional requirements for Manager:

Add one extra variable department
Override the display_details() method to display all details including department.
Expected Output Example
Name: Rahul
Salary: 50000
Department: HR'''
class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def show_details(self):
        print(f"Name : {self.__name} \n Salary :{self.__salary}")

class Manager(Employee):
    def __init__(self, name, salary,department):
        self.__department = department
        super().__init__(name, salary)

    def show_details(self):
        print(f"Department {self.__department}")
        return super().show_details()
    
m1 = Manager("Saurav",50000,"HR")
m1.show_details()

        
    