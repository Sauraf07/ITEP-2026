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
    interest_rate = 0.05
    def __init__(self, acc_num, holder_name, balance):
        self.__acc_num = acc_num
        self.__holder_name = holder_name
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
            print(f"Current Balance: {self.__balance}")
        else:
            self.__balance -= amount
            print(f"Withdrawal successful. New Balance: {self.__balance}")

    def account_summary(self):
        print(f"Account Number: {self.__acc_num}")
        print(f"Holder Name: {self.__holder_name}")
        print(f"Balance: {self.__balance}")
    
    @classmethod
    def bank_wide_interest(cls, amount):
        return amount * cls.interest_rate

    @staticmethod
    def validate_min_balance(balance):
        return balance >= 1000
    
acc1 = Bank("abc1234567890", "Saurav", 500)
acc1.deposit(2000)
acc1.withdraw(5000)
print(f"Bank-wide interest: {acc1.bank_wide_interest(1000)}")
acc1.account_summary()