'''
46. Hotel Booking System
Implement:
room types
booking
pricing
'''
from abc import *
class Hotel(ABC):
    @abstractmethod
    def roomtypes(self):
        pass
    @abstractmethod
    def booking(self):
        pass
    @abstractmethod
    def pricing(self):
        pass

class Taj(Hotel):
    def roomtypes(self):
        print("Ac And Non AC both ")
    
    def booking(self):
        print("Booking aviablable")

    def pricing(self):
        print("Price")

h1 = Taj()
h1.roomtypes()
h1.booking()
h1.pricing()