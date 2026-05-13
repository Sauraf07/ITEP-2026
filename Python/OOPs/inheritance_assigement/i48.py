'''
48. Inventory Management System

Features:

stock
suppliers
billing
'''
from abc import *
class Inventory(ABC):
    @abstractmethod
    def stock(self):
        pass
    @abstractmethod
    def suppliers(self):
        pass
    @abstractmethod
    def billing(self):
        pass
class ABCInventory(Inventory):
    def stock(self):
        print("Stock available")

    def suppliers(self):
        print("Suppliers listed")

    def billing(self):
        print("Billing system in place")
i1 = ABCInventory()
i1.stock()
i1.suppliers()
i1.billing()
