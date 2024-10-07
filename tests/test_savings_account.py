"""
Description:
Author: Jashanpreet Kaur Jattana
"""

import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):

    def setUp(self):
        self.valid_account_number = 123456
        self.valid_client_number = 67890
        self.valid_balance = 500.00
        self.valid_date_created = date.today()
        self.valid_minimum_balance = 50.00

        self.account = SavingsAccount(
            account_number=self.valid_account_number,
            client_number=self.valid_client_number,
            balance=self.valid_balance,
            date_created=self.valid_date_created,
            minimum_balance=self.valid_minimum_balance
        )

    def test_init_valid(self):
        self.assertEqual(self.account.account_number, self.valid_account_number)
        self.assertEqual(self.account.client_number, self.valid_client_number)
        self.assertEqual(self.account.balance, self.valid_balance)
        self.assertEqual(self.account._minimum_balance, self.valid_minimum_balance)
        self.assertEqual(self.account._date_created, self.valid_date_created)

    def test_init_invalid_minimum_balance(self):
        account = SavingsAccount(
            account_number=self.valid_account_number,
            client_number=self.valid_client_number,
            balance=self.valid_balance,
            date_created=self.valid_date_created,
            minimum_balance="invalid"
        )
        self.assertEqual(account._minimum_balance, 50.0)

    def test_get_service_charges_balance_greater_than_minimum(self):
        actual_charge = self.account.get_service_charges()
        expected_charge = 0.50  
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_get_service_charges_balance_equal_to_minimum(self):
        self.account.balance = self.valid_minimum_balance
        actual_charge = self.account.get_service_charges()
        expected_charge = 0.50  
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_get_service_charges_balance_less_than_minimum(self):
        self.account.balance = 49.99
        actual_charge = self.account.get_service_charges()
        expected_charge = 0.50 * 2.0  
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_str_method(self):
        expected_string = (
            f"Account Number: {self.valid_account_number} "
            f"Balance: ${self.valid_balance:.2f}\n"
            f"Minimum Balance: ${self.valid_minimum_balance:.2f} Account Type: Savings"
        )
        self.assertEqual(str(self.account), expected_string)

if __name__ == "__main__":
    unittest.main()


