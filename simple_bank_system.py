
from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def is_account_valid(self, account: int):
        return account >= 1 and account <= len(self.balance)

    def check_removal(self, account: int, money: int) -> bool:
        # assuming account is within 1 and n
        return self.balance[account - 1] >= money

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (not self.is_account_valid(account1)) or (not self.is_account_valid(account2)):
            return False

        if not self.check_removal(account1, money):
            return False

        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money

        return True
        
    def deposit(self, account: int, money: int) -> bool:
        if not self.is_account_valid(account):
            return False
        
        self.balance[account - 1] += money

        return True

    def withdraw(self, account: int, money: int) -> bool:
        if (not self.is_account_valid(account)) or (not self.check_removal(account, money)):
            return False

        self.balance[account - 1] -= money

        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)