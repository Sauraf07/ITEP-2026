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

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self):
        pass
    
class DeliverySystem(ABC):
    @abstractmethod
    def deliver(self):
        pass


