"""
Description:
Author: Jashanpreet Kaur Jattana
"""

import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    """Unit tests for the SavingsAccount class."""

    def setUp(self):
        """Set up a valid SavingsAccount instance for testing."""
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
        """Test __init__ with valid parameters."""
        self.assertEqual(self.account.account_number, self.valid_account_number)
        self.assertEqual(self.account.client_number, self.valid_client_number)
        self.assertEqual(self.account.balance, self.valid_balance)
        self.assertEqual(self.account._minimum_balance, self.valid_minimum_balance)
        self.assertEqual(self.account._date_created, self.valid_date_created)

    def test_init_invalid_minimum_balance(self):
        """Test __init__ with invalid minimum balance value."""
        account = SavingsAccount(
            account_number=self.valid_account_number,
            client_number=self.valid_client_number,
            balance=self.valid_balance,
            date_created=self.valid_date_created,
            minimum_balance="invalid"  # Invalid input
        )
        self.assertEqual(account._minimum_balance, 50.0)  # Default value should be assigned

    def test_get_service_charges_balance_greater_than_minimum(self):
        """Test service charges when balance is greater than minimum balance."""
        actual_charge = self.account.get_service_charges()
        expected_charge = 0.50  
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_get_service_charges_balance_equal_to_minimum(self):
        """Test service charges when balance is equal to minimum balance."""
        self.account.balance = self.valid_minimum_balance  # Set balance to minimum
        actual_charge = self.account.get_service_charges()
        expected_charge = 0.50  
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_get_service_charges_balance_less_than_minimum(self):
        """Test service charges when balance is less than minimum balance."""
        self.account.balance = 49.99  # Set balance below minimum
        actual_charge = self.account.get_service_charges()
        expected_charge = 0.50 * 2.0  # Premium charge
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_str_method(self):
        """Test the string representation of the SavingsAccount."""
        expected_string = (
            f"Account Number: {self.valid_account_number} "
            f"Balance: ${self.valid_balance:.2f}\n"
            f"Minimum Balance: ${self.valid_minimum_balance:.2f} Account Type: Savings"
        )
        self.assertEqual(str(self.account), expected_string)

if __name__ == "__main__":
    unittest.main()


