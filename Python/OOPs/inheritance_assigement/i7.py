'''
7. Shopping Cart System
Base:
Product
Derived:
Electronics
Grocery
Clothing
Apply discounts.
'''
class Product:
    def discount(self):
        pass
class Electronics(Product):
    def discount(self):
        print("5% Discount")

class Grocery(Product):
    def discount(self):
        print("10% Discount")

class Clothing(Product):
    def discount(self):
        print("15% Discount")

e = Electronics()
e.discount()
g = Grocery()
g.discount()
c = Clothing()
c.discount()