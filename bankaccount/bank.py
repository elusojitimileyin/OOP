from OOP.bankaccount.account import Account
from OOP.exceptions.invalid_amount_exception import InvalidAmountException
from OOP.exceptions.invalid_pin_exception import InvalidPinException


class Bank:
    def __init__(self, name):
        self.name = name
        self.number = 1
        self.accounts = []

    def register_customer(self, first_name, last_name, pin):
        name = first_name + " " + last_name
        account = Account(name, self.number, pin)
        self.accounts.append(account)
        self.number += 1
        return account

    def get_number_of_customer(self):
        return len(self.accounts)

    def check_balance(self, pin, account_number):
        account = self.find_account(account_number)
        return account.check_balance(pin)

    def deposit(self, amount, account_number):
        account = self.find_account(account_number)
        account.deposit(amount)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_number() == account_number:
                return account
        raise InvalidAmountException("No such account is found.")

    def transfer(self, amount, receiver_account_number, sender_account_number, pin):
        sender_account = self.find_account(sender_account_number)
        receiver_account = self.find_account(receiver_account_number)
        sender_account.withdraw(amount, pin)
        receiver_account.deposit(amount)

    def withdraw(self, account_number, amount, pin):
        account = self.find_account(account_number)
        account.withdraw(amount, pin)

    def remove_account(self, account_number, pin):
        account = self.find_account(account_number)
        if account.validate_pin(pin):
            raise InvalidPinException("Invalid Pin")
        self.accounts.remove(account)
