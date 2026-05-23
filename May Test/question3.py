'''
Question 3 — Abstract Class
Create an abstract class Shape.
Requirements:
Use the ABC module.
Create an abstract method:
area()
Create two child classes:
Rectangle
Circle
Implement the area() method in both classes.
Formula
Rectangle Area = length × breadth
Circle Area = π × r × r
Take input from the user and display the calculated area.'''
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

class Circle(Shape):
    def __init__(self,radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius * self.__radius
    
l = float(input("Enter the length of Rectange : "))
b = float(input("Enter the bredth of the rectangle : "))
R = Rectangle(l,b)
print(f"Area Of a Rectangel : {R.area()}")

r = float(input("Enter the radius : "))
C = Circle(r)
print(f"Area Of Circle : {C.area()}")


