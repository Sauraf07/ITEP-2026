'''
43. Railway Reservation System
Classes:
Passenger
Ticket
Train
Add booking logic.
'''
from abc import *
class Passenger(ABC):

    @abstractmethod
    def get_details(self):
        pass

class Train:

    def __init__(self, train_name, seats):
        self.train_name = train_name
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            return True
        return False

class Ticket(Passenger):

    def __init__(self, name, ticket_type, train):
        self.__name = name
        self.__ticket_type = ticket_type
        self.train = train

    def get_details(self):
        print("Passenger:", self.__name)
        print("Ticket Type:", self.__ticket_type)
        print("Train:", self.train.train_name)

    def book_ticket(self):
        if self.train.book_seat():
            print("Ticket Booked Successfully")
            self.get_details()
        else:
            print("No seats available")


t1 = Train("Rajdhani Express", 2)
p1 = Ticket("Saurav", "Sleeper", t1)
p1.book_ticket()
p2 = Ticket("Gaurav","Sleeper",t1)
p2.book_ticket()