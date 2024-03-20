import unittest
from OOP.bankaccount.account import *

class TestAccount(unittest.TestCase):
    def test_canDepositMoney(self):
        myAccount = Account("firstName", "lastName", "pin")
        myAccount.deposit(500)
        self.assertEqual(500, myAccount.check_balance("pin"))

    def test_canDepositMoneyTwice(self):
        myAccount = Account("firstName", "lastName", "pin")
        myAccount.deposit(500)
        myAccount.deposit(500)
        self.assertEqual(1000, myAccount.check_balance("pin"))

    def test_canDepositMoneyAndWithdraw(self):
        myAccount = Account("firstName", "lastName", "pin")
        myAccount.deposit(500)
        self.assertEqual(500, myAccount.check_balance("pin"))
        myAccount.withdraw(200, "pin")
        self.assertEqual(300, myAccount.check_balance("pin"))

    def test_canDepositMoneyTwiceAndWithdraw(self):
        myAccount = Account("firstName", "lastName", "pin")
        myAccount.deposit(500)
        myAccount.deposit(500)
        self.assertEqual(1000, myAccount.check_balance("pin"))
        myAccount.withdraw(200, "pin")
        self.assertEqual(800, myAccount.check_balance("pin"))

    def test_canDepositMoneyTwiceAndWithdrawTwice(self):
        myAccount = Account("firstName", "lastName", "pin")
        myAccount.deposit(500)
        myAccount.deposit(500)
        self.assertEqual(1000, myAccount.check_balance("pin"))
        myAccount.withdraw(200, "pin")
        myAccount.withdraw(200, "pin")
        self.assertEqual(600, myAccount.check_balance("pin"))

    def test_canDepositMoneyTwiceAndWithdrawNegativeNumber(self):
        myAccount = Account("firstName", "lastName", "pin")
        myAccount.deposit(500)
        myAccount.deposit(500)
        self.assertEqual(1000, myAccount.check_balance("pin"))
        with self.assertRaises(InvalidAmountException):
            myAccount.withdraw(-200, "pin")
        self.assertEqual(1200, myAccount.check_balance("pin"))

    def test_emptyAccount_withdrawMoney(self):
        myAccount = Account("firstName", "lastName", "pin")
        myAccount.deposit(500)
        self.assertEqual(500, myAccount.check_balance("pin"))
        with self.assertRaises(InsufficientFundsException):
            myAccount.withdraw(600, "pin")

    def test_emptyAccount_inputWrongPin_withdrawMoney(self):
        myAccount = Account("firstName", "lastName", "pin")
        myAccount.deposit(500)
        with self.assertRaises(InvalidPinException):
            myAccount.check_balance("pi")

        with self.assertRaises(InsufficientFundsException):
            myAccount.withdraw(600, "pin")


if __name__ == '__main__':
    unittest.main()