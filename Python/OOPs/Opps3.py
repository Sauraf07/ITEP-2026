class CS:
    def __init__(self):
        self.id = 100

    def set_name(self,name):
        self.name = name

    def display_contact(self):
        print(f"Contact {self.contact}")

obj = CS()
print(obj.__dict__)
obj.set_name('Saurav')
print(obj.__dict__)
obj.contact = 789465
print(obj.__dict__)
obj.display_contact()
