'''
8. Inventory Management System
Problem

Create product inventory software.

Requirements

Each product should contain:

product id
product name
quantity
price
Functionalities
Add stock
Reduce stock after purchase
Prevent negative stock
Calculate inventory value
Concepts Practiced
arithmetic inside classes
validations
inventory logic
'''
class Product:
    def __init__(self, product_id, name, quantity, price):
        self.__product_id = product_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price
    
    def add_stock(self, amount):
        if amount > 0:
            self.__quantity += amount
            print(f"Added {amount} units to '{self.__name}'. New quantity: {self.__quantity}")
        else:
            print("Invalid stock amount. Must be greater than zero.")
    
    def reduce_stock(self, amount):
        if 0 < amount <= self.__quantity:
            self.__quantity -= amount
            print(f"Reduced {amount} units from '{self.__name}'. New quantity: {self.__quantity}")
        else:
            print(f"Cannot reduce {amount} units. Available stock: {self.__quantity}")
    
    def calculate_inventory_value(self):
        return self.__quantity * self.__price
    
    def Details(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Quantity: {self.__quantity}")
        print(f"Price: {self.__price}")

product1 = Product(101, "Laptop", 50, 1000)
product1.Details()  
product1.add_stock(20)
product1.reduce_stock(10)
print(f"Inventory Value: {product1.calculate_inventory_value()}")
product1.reduce_stock(70)
