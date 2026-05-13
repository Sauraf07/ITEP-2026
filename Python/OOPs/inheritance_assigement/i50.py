'''
50. Cryptocurrency Wallet System

Features:

wallet
transactions
deposits
withdrawals
Implement secure transaction architecture.
'''
from abc import *
class CryptoWallet(ABC):
    @abstractmethod
    def wallet(self):
        pass
    @abstractmethod
    def transactions(self):
        pass
    @abstractmethod
    def deposits(self):
        pass
    @abstractmethod
    def withdrawals(self):
        pass
class MyCryptoWallet(CryptoWallet): 
    def wallet(self):
        print("Wallet created")

    def transactions(self):
        print("Transactions recorded")

    def deposits(self):
        print("Deposits processed")

    def withdrawals(self):
        print("Withdrawals processed")
c1 = MyCryptoWallet()
c1.wallet()
c1.transactions()
c1.deposits()
c1.withdrawals()