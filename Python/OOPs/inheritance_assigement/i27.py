'''
27. Transport Fare System
Abstract:
Transport
Derived:
Train
Flight
Bus
Implement ticket pricing.
'''
from abc import *
class Transport(ABC):
    @abstractmethod
    def fare(self):
        pass
class Train(Transport):
    def fare(self,p):
        print(f" Your Total Train Fare : {p}")
class Flight(Transport):
    def fare(self,p):
        print(f" Your Total Flight Fare : {p}")
class Bus(Transport):
    def fare(self,p):
        print(f" Your Total Bus Fare : {p}")
t = Train()
t.fare(100)     
f = Flight()
f.fare(500)
b = Bus()
b.fare(50)
