from abc import ABC, abstractmethod

class A(ABC):

    def __init__(self):
        print("Constructor of A")

    def wish(self):
        print("Welcome from class A")

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass



class B(A):

    def __init__(self):
        super().__init__()

  
    def m1(self):
        print("Implementation of m1 in class B")
        super().wish()

   
    def m2(self):
        print("Implementation of m2 in class B")



obj = B()

obj.wish()
obj.m1()
obj.m2()