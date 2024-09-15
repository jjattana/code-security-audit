"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: Jashanpreet Kaur Jattana
Date: 2024-09-14
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount  

class TestBankAccount(unittest.TestCase):

    def test_init_valid_values(self):
        account = BankAccount(12345, 67890, 100.0)
        self.assertEqual(12345, account.account_number)  # Name mangling
        self.assertEqual(67890, account.client_number)  # Name mangling
        self.assertEqual(100.0, round(account.balance, 2))  # Name mangling

    def test_init_non_numeric_balance(self):
        account = BankAccount(12345, 67890, "abc")
        self.assertEqual(0.0, round(account.balance, 2))  # Name mangling

    def test_init_non_numeric_account_number(self):
        with self.assertRaises(ValueError):
            BankAccount("abc", 67890, 100.0)

    def test_init_non_numeric_client_number(self):
        with self.assertRaises(ValueError):
            BankAccount(12345, "abc", 100.0)

    def test_account_number_getter(self):
        account = BankAccount(12345, 67890, 100.0)
        self.assertEqual(12345, account.account_number)

    def test_client_number_getter(self):
        account = BankAccount(12345, 67890, 100.0)
        self.assertEqual(67890, account.client_number)

    def test_balance_getter(self):
        account = BankAccount(12345, 67890, 100.0)
        self.assertEqual(100.0, round(account.balance, 2))

    def test_update_balance_positive_amount(self):
        account = BankAccount(12345, 67890, 100.0)
        account.update_balance(50.0)
        self.assertEqual(150.0, round(account.balance, 2))  # Name mangling

    def test_update_balance_negative_amount(self):
        account = BankAccount(12345, 67890, 100.0)
        account.update_balance(-30.0)
        self.assertEqual(70.0, round(account.balance, 2))  # Name mangling

    def test_update_balance_non_numeric(self):
        account = BankAccount(12345, 67890, 100.0)
        with self.assertRaises(ValueError):
            account.update_balance("abc")
        self.assertEqual(100.0, round(account.balance, 2))  # Name mangling

    def test_deposit_valid_amount(self):
        account = BankAccount(12345, 67890, 100.0)
        account.deposit(200.0)
        self.assertEqual(300.0, round(account.balance, 2))  # Name mangling

    def test_deposit_negative_amount(self):
        account = BankAccount(12345, 67890, 100.0)
        with self.assertRaises(ValueError):
            account.deposit(-50.0)

    def test_withdraw_valid_amount(self):
        account = BankAccount(12345, 67890, 100.0)
        account.withdraw(50.0)
        self.assertEqual(50.0, round(account.balance, 2))  # Name mangling

    def test_withdraw_negative_amount(self):
        account = BankAccount(12345, 67890, 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(-30.0)

    def test_withdraw_exceeds_balance(self):
        account = BankAccount(12345, 67890, 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(150.0)

    def test_str_method(self):
        account = BankAccount(12345, 67890, 100.0)
        self.assertEqual("Account Number: 12345 Balance: $100.00", str(account))

if __name__ == '__main__':
    unittest.main()


