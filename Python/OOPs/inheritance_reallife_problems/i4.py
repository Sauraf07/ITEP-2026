'''
4. Vehicle Parking Fee System
Problem Statement
Parking fees vary by vehicle type.
Create:
abstract class Vehicle
Child classes:
Bike
Car
Bus
Rules:
Bike → ₹10/hour
Car → ₹30/hour
Bus → ₹50/hour
'''
from abc import *
class Vehical(ABC):
    
    def __init__(self,hour):
        self.__hour = hour

    @abstractmethod
    def parking_fees(self):
        pass
        
    def get_hour(self):
        return self.__hour

class Bike(Vehical):
    def parking_fees(self):
        return self.get_hour() * 10
    
class Car(Vehical):
    def parking_fees(self):
        return self.get_hour() * 30
    
class Bus(Vehical):
    def parking_fees(self):
        return self.get_hour() * 50
    
b1 = Bike(5)
print(f"Parking fees for Bike is {b1.parking_fees()}")
print("="*10)
c1 = Car(10)
print(f"Parking fees for Car is {c1.parking_fees()}")
print("="*10)
b2 = Bus(15)
print(f"Parking fees for Bike is {b2.parking_fees()}")
