'''
22. Payment Gateway
Abstract class Payment
Derived:
CreditCard
UPI
Wallet
Implement payment processing.
'''
from abc import *
class Payment(ABC):
    @abstractmethod
    def payment_process(self):
        pass

class CreditCard(Payment):
    def payment_process(self):
        print("Fast")

class UPI(Payment):
    def payment_process(self):
        print("Moderte")
class Wallet(Payment):
    def payment_process(self):
        print("Little slow")
u = UPI()
u.payment_process()