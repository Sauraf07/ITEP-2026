from abc import *
class A:
    def __init__(self):
        pass
    def wish(self):
        pass
 
    @abstractmethod
    def m1(cls):
        print("hello")

    @abstractmethod
    def m2():
        print("hello1")

class B(A):
    def __init__(self):
      super().__init__()
      super().wish()
      super().m1()
    #   super().m2()

    @abstractmethod
    def m1(cls):
      super().m1()
      super().m2()
      super(B,cls).wish(cls)


    @staticmethod
    def m1():
      super(B,B).m1()

obj = B()
