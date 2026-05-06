class Book:
    def set_title(self,title):
        self.title = title
    def set_author(self,author):
        self.author = author
    def set_price(self,price):
        self.price = price
    def details(self):
        print(f"Book Title {self.title}")
        print(f"Author {self.author}")
        print(f"Price {self.price}")

b1 = Book()
b1.set_title("Game of thons")
b1.set_author("Saurav")
b1.set_price(1999)
b1.details()