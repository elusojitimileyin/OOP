from OOP.exceptions.insufficient_funds_exception import InsufficientFundsException
from OOP.exceptions.invalid_amount_exception import InvalidAmountException
from OOP.exceptions.invalid_pin_exception import InvalidPinException


class Account:
    def __init__(self, name, number, pin):
        self.name = name
        self.balance = 0
        self.pin = pin
        self.number = number

    def validate_pin(self, pin):
        return pin != self.pin

    def check_balance(self, pin):
        if self.validate_pin(pin):
            raise InvalidPinException("Invalid Pin")
        return self.balance

    def deposit(self, amount):
        self.validate_pin(self.pin)
        self.balance += amount
        if amount <= 0:
            raise InvalidAmountException("amount should be greater than zero")

    def withdraw(self, amount, pin):

        self.validate_pin(pin)
        self.balance -= amount
        if amount <= 0:
            raise InvalidAmountException("negative number cannot be withdrawn")
        if amount > self.balance:
            raise InsufficientFundsException("amount above balance cannot be withdrawn")

    def get_number(self):
        return self.number
