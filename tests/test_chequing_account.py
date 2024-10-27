"""
Description:
Author: Jashanpreet Kaur Jattana
"""
import sys
print("Python search paths:", sys.path)

import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class TestChequingAccount(unittest.TestCase):
    """Unit tests for the ChequingAccount class, ensuring proper initialization
    and functionality of methods."""

    def test_init_valid_attributes(self):
        """Test the initialization of ChequingAccount with valid attributes."""
        account = ChequingAccount(
            account_number="12345",
            client_number="67890",
            account_holder="Jashanpreet Jattana",
            initial_balance=500.0,
            overdraft_limit=1000.0,
            overdraft_rate=0.05,
            date_created="2023-01-01"
        )
        self.assertEqual(account.account_number, "12345")
        self.assertEqual(account.client_number, "67890")
        self.assertEqual(account.account_holder, "Jashanpreet Jattana")
        self.assertEqual(account.balance, 500.0)
        self.assertEqual(account.date_created.strftime('%Y-%m-%d'), "2023-01-01")

    def test_get_service_charges_balance_above_limit(self):
        """Test service charges when balance is above the overdraft limit."""
        account = ChequingAccount(
            account_number="12345",
            client_number="67890",
            account_holder="Jashanpreet Jattana",
            initial_balance=1500.0,  # Above the overdraft limit
            overdraft_limit=1000.0,
            overdraft_rate=0.05
        )
        expected_charge = 0.50 
        self.assertAlmostEqual(account.get_service_charges(), expected_charge, places=2)

    def test_get_service_charges_balance_below_limit(self):
        """Test service charges when balance is below the overdraft limit."""
        account = ChequingAccount(
            account_number="12345",
            client_number="67890",
            account_holder="Jashanpreet Jattana",
            initial_balance=500.0,  # Below the overdraft limit
            overdraft_limit=1000.0,
            overdraft_rate=0.05
        )
        # Assuming charge = base charge + (overdraft limit - balance) * rate
        expected_charge = 0.50 + (1000.0 - 500.0) * 0.05
        self.assertAlmostEqual(account.get_service_charges(), expected_charge, places=2)

    def test_get_service_charges_balance_equals_limit(self):
        """Test service charges when balance is equal to the overdraft limit."""
        account = ChequingAccount(
            account_number="12345",
            client_number="67890",
            account_holder="Jashanpreet Jattana",
            initial_balance=1000.0,  # Equal to the overdraft limit
            overdraft_limit=1000.0,
            overdraft_rate=0.05
        )
        expected_charge = 0.50 
        self.assertAlmostEqual(account.get_service_charges(), expected_charge, places=2)

    def test_str_method(self):   
        """Test the string representation of the ChequingAccount object."""
        account = ChequingAccount(
            account_number="12345",
            client_number="67890",
            account_holder="Jashanpreet Jattana",
            initial_balance=500.0,
            overdraft_limit=1000.0,
            overdraft_rate=0.05,
            date_created="2023-01-01"
        )
        expected_str = ("Account Number: 12345\n"
                        "Client Number: 67890\n"
                        "Account Holder: Jashanpreet Jattana\n"
                        "Balance: $500.00\n"
                        "Account Type: Chequing")
        self.assertEqual(str(account), expected_str)

if __name__ == '__main__':
    unittest.main()
