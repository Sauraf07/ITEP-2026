'''
9. ATM Machine Simulation
Problem

Design ATM software.

Requirements

Each account should have:

account number
PIN
balance
Functionalities
Login verification
Withdraw
Deposit
Change PIN
Mini statement
Additional Challenge

Lock account after 3 wrong PIN attempts.

Concepts Practiced
encapsulation mindset
validations
object state

'''
class Account:
    def __init__(self, account_number, pin, balance):
        self.__account_number = account_number
        self.__pin = pin
        self.__balance = balance
        self.__attempts = 0
        self.__locked = False
    
    def verify_login(self, input_pin):
        if self.__locked:
            print("Account is locked due to multiple failed login attempts.")
            return False
        
        if input_pin == self.__pin:
            print("Login successful.")
            self.__attempts = 0  
            return True
        else:
            self.__attempts += 1
            print(f"Incorrect PIN. Attempt {self.__attempts}/3.")
            if self.__attempts >= 3:
                self.__locked = True
                print("Account locked due to multiple failed login attempts.")
            return False
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount. Must be greater than zero.")
    
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN. Cannot change PIN.")
    
    def mini_statement(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")

account1 = Account("123456789", "1234", 1000)
account1.verify_login("1234")   
account1.deposit(500)
account1.withdraw(200)
account1.change_pin("1234", "5678")
account1.verify_login("5678")
account1.mini_statement()





        