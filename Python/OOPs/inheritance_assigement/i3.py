'''3. Employee Management

Base class Employee.

Derived:

Developer
Tester
HR

Calculate salaries differently.

'''
class Employee:
    def __init__(self,salary):
        self.__salary = salary
        
    def salary(self):
        print(f"Salary : {self.__salary}")
        
class Developer(Employee):
    def __init__(self, salary):
        super().__init__(salary)

class Tester(Employee):
    def __init__(self, salary):
        super().__init__(salary)

class Hr(Employee):
    def __init__(self, salary):
        super().__init__(salary)

d = Developer(500)
d.salary()
T = Tester(100)
h = Hr(400)
T.salary()
h.salary()
