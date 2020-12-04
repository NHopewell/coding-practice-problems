from typing import Optional

class BankAccount:

    def __init__(self, owner: str, balance: Optional[float] = None):

        self.owner = owner
        if balance: 
            self.balance = balance
        else:
            self.balance = 0.0

    def deposit(self, value):
        self.balance += value
        return self.balance

    def withdraw(self, value):
        self.balance -= value
        return self.balance


account = BankAccount("Nick")

print(account.balance)

account.deposit(10.0)
account.withdraw(3.0)

print(account.balance)