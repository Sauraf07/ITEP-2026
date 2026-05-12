'''
24. ATM System
Abstract:
ATM
Derived.
SBIATM
HDFCATM
Implement banking operations.
'''
from abc import *
class ATM(ABC):
    @abstractmethod
    def operatin(self):
        pass
class SBIATM(ATM):
    def operatin(self):
        print("SBI ATM")

class HDFCATM(ATM):
    def operatin(self):
        print("HDFC ATM")

a = SBIATM()
a.operatin()
