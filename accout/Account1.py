class Account1:

    def __init__(self):
        self.balance = 0

    def get_Balance(self):
        return self.balance

    def deposit(self, amount: int):
        if amount >= 0:
            self.balance += amount
