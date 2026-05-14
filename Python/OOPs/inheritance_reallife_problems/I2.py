'''
2. Delivery Charge Calculator
Problem Statement

A delivery company calculates delivery charges differently.

Create:

abstract class Delivery

Child classes:

BikeDelivery
TruckDelivery
DroneDelivery

Rules:

Bike → ₹5/km
Truck → ₹15/km
Drone → ₹20/km
Input Example

Distance = 10 km

Expected Output
Bike Delivery Charge = 50
Truck Delivery Charge = 150
'''
from abc import ABC, abstractmethod     
class Delivery(ABC):
    def __init__(self, distance):
        self.__distance = distance

    @abstractmethod
    def calculate_charge(self):
        pass

    def get_distance(self):
        return self.__distance
    
class BikeDelivery(Delivery):
    def calculate_charge(self):
        return self.get_distance() * 5

class TruckDelivery(Delivery):
    def calculate_charge(self):
        return self.get_distance() * 15

class DroneDelivery(Delivery):
    def calculate_charge(self):
        return self.get_distance() * 20

d1 = BikeDelivery(10)
d2 = TruckDelivery(10)
d3 = DroneDelivery(10)

print("Bike Delivery Charge =", d1.calculate_charge())
print("Truck Delivery Charge =", d2.calculate_charge())
print("Drone Delivery Charge =", d3.calculate_charge())
