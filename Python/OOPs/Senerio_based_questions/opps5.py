'''
5. Library Management System
Problem
Design a library system.
Requirements
Each book should contain:
book id
title
author
availability status
Functionalities
Issue book
Return book
Display availability
Count total books using class variable
Additional Challenge
Prevent issuing already issued books.
Concepts Practiced
object state changes
boolean flags
class variables
'''
class Book:
    total_books = 0
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__is_available = True
        Book.total_books += 1
    
    def issue_book(self):
        if self.__is_available:
            self.__is_available = False
            print(f"Book '{self.__title}' issued successfully.")
        else:
            print(f"Book '{self.__title}' is already issued.")
    
    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print(f"Book '{self.__title}' returned successfully.")
        else:
            print(f"Book '{self.__title}' was not issued.")
    
    def display_availability(self):
        status = "available" if self.__is_available else "not available"
        print(f"Book '{self.__title}' is {status}.")
    
    @classmethod
    def total_books_count(cls):
        return cls.total_books
    
book1 = Book(101, "Python", "Guido")
book1.display_availability()
book1.issue_book()
book1.display_availability()
book1.issue_book()
book1.return_book()
book1.display_availability()
print(f"Total Books in Library: {Book.total_books_count()}")