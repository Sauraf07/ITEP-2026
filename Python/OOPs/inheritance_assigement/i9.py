'''
9. Library Management
Parent:
LibraryItem
Derived:
Book
Magazine
Newspaper
Implement borrowing system.
'''
class LibraryItem:

    def __init__(self, title):
        self.title = title
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f"{self.title} borrowed")
        else:
            print(f"{self.title} already borrowed")


class Book(LibraryItem):
    pass

class Magazine(LibraryItem):
    pass

class Newspaper(LibraryItem):
    pass

b = Book("Python Book")
m = Magazine("Tech Magazine")
n = Newspaper("Daily News")

b.borrow()
m.borrow()
n.borrow()