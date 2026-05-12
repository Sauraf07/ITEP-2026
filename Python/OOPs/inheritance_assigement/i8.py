'''
8. Online Food Delivery
Parent:
FoodItem
Derived:
Pizza
Burger
Sandwich
Calculate total bill.
'''
class FoodItem:
    def bill(self,bill):
        self.__bill = bill
        print(f"Your Total bill : {self.__bill}")    

class Pizza(FoodItem):
    def bill(self, bill):
        return super().bill(bill)

class Burger(FoodItem):
    def bill(self, bill):
        return super().bill(bill)

class Sandwich(FoodItem):
    def bill(self, bill):
        return super().bill(bill)

p = Pizza()
p.bill(50)
    