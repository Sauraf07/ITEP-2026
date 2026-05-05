class Calculator:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def ADD(self):
        print(f"Addition : {self.__a + self.__b}")

    def Sub(self):
         print(f"Sub : {self.__a - self.__b}")
        
    def Multi(self):
        print(f"Multi : {self.__a * self.__b}")

    def Divide(self):
         print(f"Divide : {self.__a / self.__b}")

        
obj = Calculator(10,23)
obj.ADD()
obj.Sub()
obj.Multi()
obj.Divide()