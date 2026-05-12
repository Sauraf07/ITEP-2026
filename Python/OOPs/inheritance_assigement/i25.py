'''25. Ride Booking App
Abstract:
Ride
Derived:
BikeRide
CabRide
AutoRide
Calculate fare.
'''
from abc import *
class Ride(ABC):
    @abstractmethod
    def fare(self):
        pass
class BikeRide(Ride):
    def fare(self,p):
        print(f" Your Total bike Fare : {p}")

class CarRide(Ride):
    def fare(self,p):
        print(f" Your Total Car Fare : {p}")

class AutoRide(Ride):
    def fare(self,p):
        print(f" Your Total  auto Fare : {p}")

c = CarRide()
c.fare(50)
