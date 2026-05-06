class Employee:
    def set_id(self,id):
        self.__id = id
    def set_name(self,name):
        self.__name = name
    def set_salary(self,salary):
        self.__salary = salary
    def Emp_details(self):
        print(f"Name : {self.__name}")
        print(f"id : {self.__id}")
        print(f"Salary : {self.__salary}")

e1 = Employee()
e1.set_id(101)
e1.set_name("saurav")
e1.set_salary(50000000)
e1.Emp_details()