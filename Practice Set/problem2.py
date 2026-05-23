'''
2. Food Delivery App
Scenario
A food app has:
Veg Restaurant
Non-Veg Restaurant
Dessert Shop
Each restaurant:
delivers food differently
calculates bill differently
Problem
Create:
abstract class Restaurant
abstract methods:
prepare_food()
calculate_bill()
'''
from abc import *
class Restaurant(ABC):
    @abstractmethod
    def prepare_food(self):
        pass

    @abstractmethod
    def calculate_bill(self):
        pass

class Veg_Res(Restaurant):
    def prepare_food(self):
        print("Veg Food Ready ")

    def calculate_bill(self,bill):
        print(f"You Total Bill is {bill}")

class Non_Veg_Res(Restaurant):
    def prepare_food(self):
        print("Veg Food Ready ")

    def calculate_bill(self,bill):
        print(f"You Total Bill is {bill}")

v1 = Veg_Res()
v1.prepare_food()
v1.calculate_bill(52)

v2 = Non_Veg_Res()
v2.prepare_food()
v2.calculate_bill(50)