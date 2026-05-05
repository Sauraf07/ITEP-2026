class Product:
    def __init__(self):
        self.productId = None
        self.name = None
        self.quantity = 0
        self.price = 0.0

    def set_productId(self, productId):
        self.productId = productId

    def set_name(self, name):
        self.name = name

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_price(self, price):
        self.price = price

    def calculate_total_value(self):
        return self.quantity * self.price


p = Product()
p.set_productId(101)
p.set_name("Laptop")
p.set_quantity(5)
p.set_price(50000)

print("Total Value:", p.calculate_total_value())