class Parent:
    def __init__(self):
        print("Parent called..")

class Child(Parent):
    def __init__(self):
        print("Child class..")

c1 = Child()
c1.__init__()