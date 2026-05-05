class Employee:
    def __init__(self,id,name,salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def Display(self):
        print(f"Id {self.__id}")
        print(f"Name {self.__name}")
        print(f"Salary {self.__salary}")

E1 = Employee(1,"saurav",5000)
E1.Display()        