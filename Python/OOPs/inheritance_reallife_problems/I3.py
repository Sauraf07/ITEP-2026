'''
3. Electricity Bill Generator
Problem Statement
Electricity bills are calculated differently for:
Residential users
Commercial users
Industrial users
Create abstract class ElectricityBill.
Rules
Residential:
Bill=Units x 5
Commercial:
Bill=Units x 8
Industrial:
Bill=Units x 12
Concepts
Runtime polymorphism
Real-world billing logic
'''
from abc import *
class ElectricityBill(ABC):
    def __init__(self,unit):
        self.__unit = unit
    @abstractmethod
    def Total_bill(self):
        pass
    def get_unit(self):
        return self.__unit
    
class Residential(ElectricityBill):
    def Total_bill(self):
       return self.get_unit() * 5

class Commercial(ElectricityBill):
    def Total_bill(self):
        return self.get_unit() * 8

class Industrial(ElectricityBill):
    def Total_bill(self):
        return self.get_unit() * 12

        
r1 = Residential(5)
c1 = Commercial(10)
i1 = Industrial(15)
print(f"Total Residential bill {r1.Total_bill()}")
print(f"Total Commercial bill {c1.Total_bill()}")
print(f"Total Industrial bill {i1.Total_bill()}")
