'''
5. Online Shopping Discount System
Problem Statement
Different customer types receive different discounts.
Create:
abstract class Customer
Child:
RegularCustomer
PremiumCustomer
VIPCustomer
Rules:
Regular → 5%
Premium → 10%
VIP → 20%
'''
from abc import *
class Customer(ABC):
    def __init__(self,amont):
        self.__amount = amont

    @abstractmethod
    def discount(self):
        pass

    def get_amount(self):
        return self.__amount

class Regular(Customer):
    def discount(self):
        print("You will Get 5% of Discount")
        return self.get_amount() - (self.get_amount()*5)/100
    
class Premium(Customer):
    def discount(self):
        print("You will Get 10% of discount ")
        return self.get_amount() - (self.get_amount()*10)/100

class VIP(Customer):
    def discount(self):
        print("You will Get 20% of discount ")
        return self.get_amount() - (self.get_amount()*20)/100

c1 = Regular(50)
print(f"Discount : {c1.discount()}")
print("="*20)
p1 = Premium(200)
print(f"Discount : {p1.discount()}")
print("="*20)
v1 = VIP(400)
print(f"Discount : {v1.discount()}")
        