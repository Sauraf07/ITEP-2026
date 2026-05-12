'''
45. Food Ordering Application
Implement:
menu
orders
payment
discounts
'''
from abc import *
class FoodOrder(ABC):
    @abstractmethod
    def menu(self):
        pass

    @abstractmethod
    def orders(self):
        pass

    @abstractmethod
    def payment(self):
        pass

    @abstractmethod
    def discounts(self):
        pass
class FastFood(FoodOrder):
    def menu(self):
        print("Fast Food Menu")

    def orders(self):
        print("Fast Food Orders")

    def payment(self):
        print("Fast Food Payment")

    def discounts(self):
        print("Fast Food Discounts")
f = FastFood()  
f.menu()
f.orders()
f.payment()
f.discounts()
