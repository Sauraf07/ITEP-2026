'''
31. Drawable Interface
Interface:
draw()
Implement:
Circle
Rectangle
Line
'''
from abc import *
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass
class Circle(Drawable):
    def draw(self):
        print("Drawing Circle")

class Rectangle(Drawable):
    def draw(self):
        print("Drawing Rectangle")
class Line(Drawable):
    def draw(self):
        print("Drawing Line")
        
c = Circle()
c.draw()
r = Rectangle()
r.draw()
l = Line()
l.draw()