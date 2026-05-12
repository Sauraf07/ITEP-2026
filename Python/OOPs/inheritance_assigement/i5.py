'''
5. Banking System
Parent:
BankAccount
Child:
SavingsAccount
CurrentAccount
Implement withdrawal rules.
'''
class BankAccount:
    def withdrawal(self):
        pass
class SavivngAccount(BankAccount):
    def withdrawal(self):
        print("Limited")
class CurrentAccount(BankAccount):
    def withdrawal(self):
        print("Limit Lesss")

P = SavivngAccount()
P.withdrawal()
S = CurrentAccount()
S.withdrawal()