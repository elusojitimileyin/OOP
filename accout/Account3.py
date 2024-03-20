from decimal import Decimal


class Account:
    def __init__(self, name, balance: Decimal):
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance < Decimal(0.00):
            raise ValueError("amount cannot be less than 0")
        self._balance = balance

    def __str__(self):
        return f"Name: {self.name} Balance: {self.balance}"

    def validate(amount):
        if amount < Decimal(0.0):
            raise ValueError("Invalid amount")
        return amount
a1 = Account("A", Decimal(10))
print(a1)