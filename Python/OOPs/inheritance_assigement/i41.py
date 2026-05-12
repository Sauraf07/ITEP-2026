'''
41. Cab Booking Application
Features:
User booking
Driver assignment
Fare calculation
Use:
inheritance
abstraction
polymorphism
'''
from abc import *
class CabBooking(ABC):
    @abstractmethod
    def user_booking(self):
        pass
    @abstractmethod
    def driver_assignment(self):
        pass
    @abstractmethod
    def fare_calculation(self):
        pass   

class Uber(CabBooking):
    def user_booking(self):
        print("User booking by Uber")
    def driver_assignment(self):
        print("Driver assignment by Uber")
    def fare_calculation(self):
        print("Fare calculation by Uber")

class Ola(CabBooking):  
    def user_booking(self):
        print("User booking by Ola")
    def driver_assignment(self):
        print("Driver assignment by Ola")
    def fare_calculation(self):
        print("Fare calculation by Ola")
        
u = Uber()
u.user_booking()
u.driver_assignment()
u.fare_calculation()
o = Ola()
o.user_booking()
o.driver_assignment()
o.fare_calculation()
