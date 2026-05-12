'''
36. Payment Interface
Methods
pay()
Implement:
PayPal
Stripe
Razorpay
'''
from abc import *
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class PayPal(Payment):
    def pay(self):
        print("Payment by Paypal")

class Strip(Payment):
    def pay(self):
        print("Payment by Strip")

class Razorpay(Payment):
    def pay(self):
        print("Payemt by Razorpay")

p1 = PayPal()
p1.pay()
p2 =  Strip()
p2.pay()
p3 = Razorpay()
p3.pay()