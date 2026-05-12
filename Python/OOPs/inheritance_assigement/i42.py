'''
42. E-Commerce Order Processing
Implement:
products
orders
payment methods
delivery system
'''
from abc import *
class Product(ABC):
    @abstractmethod
    def details(self):
        pass

    @abstractmethod
    def deliver(self):
        pass
    @abstractmethod
    def process_order(self):
        pass
    @abstractmethod
    def make_payment(self):
        pass

class Electronins(Product):
    def process_order(self):
        print("Order procesed")

    def details(self):
        print("Laptop")
    
    def deliver(self):
        print("Order Delivered")

    def make_payment(self):
        print("Payment done")

p = Electronins()
p.details()
p.deliver()
p.make_payment()
p.process_order()
