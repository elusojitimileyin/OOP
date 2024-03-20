import unittest

from accout.Account1 import Account1


class TestAccount1(unittest.TestCase):

    def test_newAccountBalanceIsZero(self):
        timi_account: Account1 = Account1()
        self.assertEqual(0, timi_account.get_Balance())

    def test_newAccountBalanceCanDeposit(self):
        timi_account: Account1 = Account1()
        timi_account.deposit(10_000)
        self.assertEqual(10_000, timi_account.get_Balance())

    def test_newAccountBalanceCanDepositTwice(self):
        timi_account: Account1 = Account1()
        timi_account.deposit(10_000)
        timi_account.deposit(20_000)
        self.assertEqual(30_000, timi_account.get_Balance())

    def test_newAccountBalanceCanDepositNegativeAmount(self):
        timi_account: Account1 = Account1()
        timi_account.deposit(-10_000)
        self.assertEqual(0, timi_account.get_Balance())