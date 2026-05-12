'''
14. Multiple Inheritance Example
Classes:
Father
Mother
Child(Father, Mother)
Access methods from both.
'''
class Father:
    def role(self):
        print("Father")

class Mother:
    def role(self):
        print("Mother")

class Child(Father,Mother):
    def role(self):
        return super().role()
c = Child()
c.role()