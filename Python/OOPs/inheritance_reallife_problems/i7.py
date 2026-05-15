'''
7. Cab Fare Calculator
Problem Statement
Cab fares differ based on ride type.
Create:
abstract class Ride
Child:
MiniRide
SedanRide
SUVRide
Rules:
Mini → ₹10/km
Sedan → ₹15/km
SUV → ₹20/km
'''
from abc import *
class Ride(ABC):
    def __init__(self,km):
        self.__km = km
    
    @abstractmethod
    def total_fare(self):
        pass

    def get_km(self):
        return self.__km

class MiniRide(Ride):
    def total_fare(self):
        print("For Mini Ride fare is ₹10/km ")
        print(f"Your total Fares of MiniRide is {self.get_km() * 10}")
    
class SedanRide(Ride):
    def total_fare(self):
        print("For Sedan Ride fare is ₹15/km ")
        print(f"Your total Fares of Sedan Ride is {self.get_km() * 15}")
    
class SUVRide(Ride):
    def total_fare(self):
        print("For SUV Ride fare is ₹20/km ")
        print(f"Your total Fares of SUV Ride is {self.get_km() * 20}")

r1 = MiniRide(10)
r2 = SedanRide(15)
r3 = SUVRide(20)
r1.total_fare()
print("="*20)
r2.total_fare()
print("="*20)
r3.total_fare()    

        