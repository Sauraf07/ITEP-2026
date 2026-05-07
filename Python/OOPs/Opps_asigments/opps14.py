'''
2. Bank Account Simulation
Problem
Design a banking system using OOP.
Requirements
Each account should contain:
account number
holder name
balance
Functionalities
Deposit money
Withdraw money
Prevent withdrawal if balance insufficient
Display account summary
Maintain bank-wide interest rate as class variable
Add static method to validate minimum balance rule
Concepts Practiced
object state management
static methods
class variables
validations
'''
class Bank:
    def __init__(self,ac_num,Name,Balance):
        self.__ac_num = ac_num
        self.__Name = Name
        self.__Balance = Balance
    
    def Details(self):
        print(f"A/C : {self.__ac_num}")
        print(f"Name : {self.__Name}")
        print(f"Balance : {self.__Balance}")
    
    def Deposit_money(self,money):
        self.__Balance = self.__Balance + money
        print(f"Your Total Balance is {self.__Balance}")

    def Withwarw_money(self,money):
        if self.__Balance > money:
            self.__Balance = self.__Balance - money
            print("Widthdrawl Successful...")
            print(f"Your Total Balance is {self.__Balance}")
        else:
            print("Widthdrawl Failed...")
            print(f"You Don't have enough Balance ")
    
B1 = Bank("abc1346","Saurav",100)
B1.Deposit_money(100)
B1.Withwarw_money(50)
B1.Details()
        