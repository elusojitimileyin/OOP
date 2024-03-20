import unittest

from OOP.bankaccount.bank import Bank
from OOP.exceptions.invalid_amount_exception import InvalidAmountException


class BankTest(unittest.TestCase):

    def test_registerCustomer_numberOfCustomer(self):
        myBank = Bank("TIMI Bank")
        self.assertEqual(0, myBank.get_number_of_customer())
        myBank.register_customer("firstName", "lastName", "pin")
        self.assertEqual(1, myBank.get_number_of_customer())

    def test_registerCustomerTwo_numberOfCustomer(self):
        myBank = Bank("TIMI Bank")
        self.assertEqual(0, myBank.get_number_of_customer())
        myBank.register_customer("firstName", "lastName", "pin")
        myBank.register_customer("firstName", "lastName", "pin")
        self.assertEqual(2, myBank.get_number_of_customer())

    def test_registerCustomerTwo_removeOneCustomer_numberOfCustomer(self):
        myBank = Bank("TIMI Bank")
        self.assertEqual(0, myBank.get_number_of_customer())
        myBank.register_customer("firstName", "lastName", "pin")

        myBank.r(1, "pin")
        self.assertEqual(1, myBank.get_number_of_customer())

    def test_register_customer_two_number_of_customer_find_customer(self):
        myBank = Bank("TIMI Bank")
        self.assertEqual(0, myBank.get_number_of_customer())
        myBank.register_customer("firstName", "last", "pin")
        myBank.register_customer("bobo", "ww", "123")
        self.assertEqual(2, myBank.get_number_of_customer())
        with self.assertRaises(InvalidAmountException):
            myBank.find_account(999)
        self.assertEqual(2, myBank.get_number_of_customer())

    def test_registerCustomer_deposit(self):
        myBank = Bank("TIMI Bank")
        self.assertEqual(0, myBank.get_number_of_customer())
        account1 = myBank.register_customer("firstName", "lastName", "1234")
        self.assertEqual(1, myBank.get_number_of_customer())
        account_number = account1.get_number()
        myBank.deposit(2000, account_number)
        self.assertEqual(myBank.check_balance("1234", account_number), 2000)


if __name__ == '__main__':
    unittest.main()
