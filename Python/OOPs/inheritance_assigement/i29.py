'''
29. Employee Attendance
Abstract:
Employee
Derived:
FullTimeEmployee
PartTimeEmployee
Calculate working hours.
'''
from abc import *
class Employee(ABC):
    @abstractmethod
    def working(self):
        pass
class FullTime(Employee):
    def working(self):
        print("Working hours 8 ")

class PartTime(Employee):
    def working(self):
        print("Working Hours 4")
f = FullTime()
f.working()
p = PartTime()
p.working()
