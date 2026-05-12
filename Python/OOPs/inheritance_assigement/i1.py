'''1. Animal Sound System

Create parent class Animal and child classes:

Dog
Cat
Cow

Override sound() method.
'''
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")
        
class Cat(Animal):
    def sound(self):
        print("Meaw")

class Cow(Animal):
    def sound(self):
        print("Mow")

A = Dog()
A.sound()
C = Cat()
C.sound()
W = Cow()
W.sound()