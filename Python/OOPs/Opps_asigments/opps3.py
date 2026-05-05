class Account:
    def __init__(self):
        self.__Name = "Saurav"
        self.__Ac_Number = 12345678
        self.__Balance = 5000

    def dalance(self):
        print(f"Name : {self.__Name} \n A/C : {self.__Ac_Number} \n Balance : {self.__Balance} ")

A1 = Account()
A1.dalance()
