'''
21. Shape Area Calculator
Abstract class Shape.
Derived:
Circle
Rectangle
Triangle
Implement area calculation.
'''
from abc import *
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self,r):
        print(f"Area of Circle {3.14*r*r}")

class Recatnge(Shape):
    def area(self,l,b):
        print(f"Area of Rectangele : {l*b}")

class Triangle(Shape):
    def area(self,b,h):
        print(f"Area of Triangel : {1/2 * b * h}")
c = Circle()
c.area(4)
r = Recatnge()
r.area(5,6)
t = Triangle()
t.area(2,5)

        
        
