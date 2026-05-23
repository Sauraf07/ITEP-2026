'''1. Online Payment System
Scenario
A shopping website supports:
Credit Card
UPI
PayPal
All payment methods:
process payment
generate receipt
But each works differently.
Concepts Used
Abstract Class
Method Overriding
Inheritance
Problem Statement
Create:
abstract class Payment
abstract method pay()
subclasses:
CreditCard
UPI
PayPal
Each class should implement its own payment logic.'''
from abc import *
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCard(Payment):
    def pay(self,amount):
        print(f"Paid {amount} Succesfully")

class UPI(Payment):
    def pay(self,amount):
        print(f"Paid {amount} Succesfully")

class PayPal(Payment):
     def pay(self,amount):
        print(f"Paid {amount} Succesfully")

p1 = CreditCard()
p1.pay(50)
p2 = UPI()
p2.pay(80)
p3 = PayPal()
p3.pay(100)
