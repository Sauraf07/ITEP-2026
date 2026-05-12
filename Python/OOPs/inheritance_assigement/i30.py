'''
30. Restaurant Management
Abstract:
Restaurant
Derived:
PizzaRestaurant
BurgerRestaurant
Prepare food differently.
'''
from abc import *
class Restraunt(ABC):
    @abstractmethod
    def p_food(self):
        pass
class Pizza(Restraunt):
    def p_food(self):
        print(" Make Pizza")
class Burger(Restraunt):
    def p_food(self):
        print("Make Burger")
p = Pizza()
p.p_food()
b = Burger()
b.p_food()