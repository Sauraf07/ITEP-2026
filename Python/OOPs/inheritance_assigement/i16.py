'''
16. E-commerce User Roles
User
Seller(User)
PremiumSeller(Seller)
Add premium benefits.
'''
class User:
    def premium(self):
        pass
class Saller(User):
    def premium(self):
        print("I am the Saller")

class PremiumSaller(Saller):
    def premium(self):
        print("I am the Premium Saller")

s = Saller()
s.premium()