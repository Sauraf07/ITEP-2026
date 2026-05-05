class Book:
    def __init__(self,title,author,price):
        self.__title = title
        self.__author = author
        self.__price = price

    def Book_details(self):
        print(f"Book Title : {self.__title}")
        print(f"Author : {self.__author}")
        print(f"Price : {self.__price}")

B1 = Book("Dragons","saurav",199)
B1.Book_details()
