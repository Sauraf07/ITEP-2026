'''
6. Movie Ticket Booking System
Problem

Create a movie booking system.

Requirements

Each movie should have:

movie name
total seats
available seats
Functionalities
Book tickets
Cancel tickets
Prevent overbooking
Display seat availability
Concepts Practiced
state updates
validations
object behavior
'''
class Movie:    
    def __init__(self, name, total_seats):
        self.__name = name
        self.__total_seats = total_seats
        self.__available_seats = total_seats
    
    def book_tickets(self, num_tickets):
        if num_tickets <= self.__available_seats:
            self.__available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for '{self.__name}'.")
        else:
            print(f"Cannot book {num_tickets} tickets. Only {self.__available_seats} seats available.")
    
    def cancel_tickets(self, num_tickets):
        if num_tickets <= (self.__total_seats - self.__available_seats):
            self.__available_seats += num_tickets
            print(f"{num_tickets} tickets cancelled for '{self.__name}'.")
        else:
            print(f"Cannot cancel {num_tickets} tickets. Only {(self.__total_seats - self.__available_seats)} tickets are booked.")
    
    def display_availability(self):
        print(f"Movie: '{self.__name}' | Available Seats: {self.__available_seats}/{self.__total_seats}")
        
movie1 = Movie("Inception", 100)
movie1.display_availability()   
movie1.book_tickets(30)
movie1.display_availability()
movie1.book_tickets(80)
movie1.cancel_tickets(10)
movie1.display_availability()
movie1.cancel_tickets(25)