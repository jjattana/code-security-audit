"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: Jashanpreet Kaur Jattana
Date: 2024-09-14
Usage: To execute all tests in the terminal execute 
the following command:python -m unittest tests/test_
    bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount  

class TestBankAccount(unittest.TestCase):

    def test_init_valid_values(self):
        """
        Ensures that class BankAccount is initilized correctly with correct values.
        """
        account = BankAccount(12345, 67890, 500.0)
        self.assertEqual(12345, account.account_number)  
        self.assertEqual(67890, account.client_number)  
        self.assertEqual(500.0, round(account.balance, 2))  

    def test_init_non_numeric_balance(self):
        """
        Ensures that incoming value can be successfully converted to a float.
        """
        account = BankAccount(12345, 67890, "abc")
        self.assertEqual(0.0, round(account.balance, 2))  

    def test_init_non_numeric_account_number(self):
        """
        Ensures that when account_number is not an integer, raise ValueError.
        """
        with self.assertRaises(ValueError):
            BankAccount("abc", 67890, 500.0)

    def test_init_non_numeric_client_number(self):
        """
        Ensures that when client_number is not an integer, raise ValueError.
        """
        with self.assertRaises(ValueError):
            BankAccount(12345, "abc", 500.0)

    def test_account_number_getter(self):
        """
        Ensures that correct value is being returned by account number getter.
        """
        account = BankAccount(12345, 67890, 500.0)
        self.assertEqual(12345, account.account_number)

    def test_client_number_getter(self):
        """
        Ensures that correct value is being returned by client number getter.
        """
        account = BankAccount(12345, 67890, 500.0)
        self.assertEqual(67890, account.client_number)

    def test_balance_getter(self):
        """
        Ensures that correct value is being returned by balance getter.
        """
        account = BankAccount(12345, 67890, 500.0)
        self.assertEqual(500.0, round(account.balance, 2))

    def test_update_balance_positive_amount(self):
        """
        Ensures that the amount by which balance is updated is a positive amount.
        """
        account = BankAccount(12345, 67890, 500.0)
        account.update_balance(100.0)
        self.assertEqual(600.0, round(account.balance, 2))  

    def test_update_balance_negative_amount(self):
        """
        Ensures that the amount by which balance is updated is a negative amount.
        """
        account = BankAccount(12345, 67890, 500.0)
        account.update_balance(-50.0)
        self.assertEqual(450.0, round(account.balance, 2))  

    def test_update_balance_non_numeric(self):
        """
        Ensures that when a non_numeric amount is given to update balance, ValueError is raised.
        """
        account = BankAccount(12345, 67890, 500.0)
        with self.assertRaises(ValueError):
            account.update_balance("abc")
        self.assertEqual(500.0, round(account.balance, 2))  

    def test_deposit_valid_amount(self):
        """
        Ensures that the balance is correctly updated with a valid amount by the deposit method.
        """
        account = BankAccount(12345, 67890, 500.0)
        account.deposit(200.0)
        self.assertEqual(700.0, round(account.balance, 2))  

    def test_deposit_negative_amount(self):
        """
        Ensures that when a negative amount is deposited, ValueError is raised.
        """
        account = BankAccount(12345, 67890, 500.0)
        with self.assertRaises(ValueError):
            account.deposit(-50.0)

    def test_withdraw_valid_amount(self):
        """
        Ensures that the balance is correctly updated with a valid amount by the withdraw method.
        """
        account = BankAccount(12345, 67890, 500.0)
        account.withdraw(200.0)
        self.assertEqual(300.0, round(account.balance, 2))  

    def test_withdraw_negative_amount(self):
        """
        Ensures that on withdrawl of a negative amount, ValueError is raised.
        """
        account = BankAccount(12345, 67890, 500.0)
        with self.assertRaises(ValueError):
            account.withdraw(-50.0)

    def test_withdraw_exceeds_balance(self):
        """
        Ensures that when the withdrawl amount is more than the balance, ValueError is raised.
        """
        account = BankAccount(12345, 67890, 500.0)
        with self.assertRaises(ValueError):
            account.withdraw(600.0)

    def test_str_method(self):
        """
        Ensures __str__ method returns correct string representation of account number and balance.
        """
        account = BankAccount(12345, 67890, 500.0)
        self.assertEqual("Account Number: 12345 Balance: $500.00", str(account))

if __name__ == '__main__':
    unittest.main()


