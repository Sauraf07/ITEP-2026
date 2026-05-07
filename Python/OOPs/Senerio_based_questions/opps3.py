'''
3. Online Shopping Cart
Problem
Create a shopping cart system.
Requirements
A cart should:
store customer name
maintain list of products
maintain total bill
Functionalities
Add product
Remove product
Calculate final amount
Apply discount using static method
Track total carts created
Concepts Practiced
list inside object
object interaction
static method
class variable
'''
class Shopping_Cart:
    total_carts = 0
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.__products = []
        self.__total_bill = 0
        Shopping_Cart.total_carts += 1
    
    def add_product(self, product_name, price):
        self.__products.append((product_name, price))
        self.__total_bill += price
    
    def remove_product(self, product_name):
        for product in self.__products:
            if product[0] == product_name:
                self.__products.remove(product)
                self.__total_bill -= product[1]
                break
    
    def calculate_final_amount(self):
        return self.__total_bill

    @staticmethod
    def apply_discount(amount, discount_percentage):
        return amount - (amount * (discount_percentage / 100))
    
    def Details(self):
        print(f"Customer Name : {self.__customer_name}")
        print(f"Products : {self.__products}")
        print(f"Bill : {self.__total_bill}")



cart1 = Shopping_Cart("Saurav")
cart1.add_product("Laptop", 1000)   
cart1.add_product("Mouse", 100)
cart1.remove_product("Mouse")
final_amount = cart1.calculate_final_amount()
discounted_amount = Shopping_Cart.apply_discount(final_amount, 10)
cart1.Details()
print(f"Final Amount after discount: {discounted_amount}")
  