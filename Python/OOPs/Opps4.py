class CS:
    def __init__(self,id,name,contact,ac):
        self.id = id
        self.name = name
        self.contact = contact
        self.ac = ac

    def display_info(self):
        print(f"Id {self.id}")
        print(f"Name {self.name}")
        print(f"Contact {self.contact}")
        print(f"AC {self.ac}")
id = int(input("Enter The id: "))
name = input("Enter your name : ")
contact = int(input("Enter contact no. "))
ac = input("Enter your acount no. ")
obj = CS(id,name,contact,ac)
obj.display_info()