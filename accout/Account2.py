from decimal import Decimal


class Account:
    def __init__(self, name: str, balance: Decimal):
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount <= Decimal(0.00):
            raise ValueError("amount cannot be less than 0")
        self.__balance += amount


a1 = Account('miriam', Decimal(500))
print(a1.balance)
a1.balance = 1000
print(a1.balance)


