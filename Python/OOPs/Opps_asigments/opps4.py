class Car:
    def __init__(self):
        self.__brand = "BMW"
        self.__model = "Xyz"
        self.__year = 2026
    def info(self):
        print(f"Brand : {self.__brand}")
        print(f"Model : {self.__model}")
        print(f"Year : {self.__year}")

C1 = Car()
C1.info()        