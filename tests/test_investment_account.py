"""
Description:
Author: Jashanpreet Kaur Jattana
"""

import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        """Set up test case with valid parameters."""
        self.valid_account_number = 12345
        self.valid_client_number = 67890
        self.valid_balance = 500.00
        self.valid_date_created = date.today()  
        self.valid_management_fee = 2.00  
        self.account = InvestmentAccount(
            self.valid_account_number,
            self.valid_client_number,
            self.valid_balance,
            self.valid_date_created,
            self.valid_management_fee
        )

    def test_init_valid(self):
        """Test __init__ with valid parameters."""
        self.assertEqual(self.account.account_number, self.valid_account_number)
        self.assertEqual(self.account.client_number, self.valid_client_number)
        self.assertEqual(self.account._balance, self.valid_balance)
        self.assertEqual(self.account.date_created, self.valid_date_created)
        self.assertEqual(self.account.management_fee, self.valid_management_fee)

    def test_init_invalid_management_fee(self):
        """Test __init__ with invalid management fee type."""
        with self.assertRaises(ValueError):
            InvestmentAccount(self.valid_account_number, self.valid_client_number, self.valid_balance, self.valid_date_created, management_fee="invalid")

    def test_get_service_charges_more_than_ten_years(self):
        """Test get_service_charges when date created is more than 10 years ago."""
        old_date = date.today() - timedelta(days=365 * 11)  # More than 10 years ago
        account = InvestmentAccount(self.valid_account_number, self.valid_client_number, self.valid_balance, old_date)
        expected_charge = InvestmentAccount.BASE_SERVICE_CHARGE  # $2.50
        actual_charge = account.get_service_charges()
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_get_service_charges_exactly_ten_years(self):
        """Test get_service_charges when date created is exactly 10 years ago."""
        ten_years_ago = date.today() - timedelta(days=365 * 10)
        account = InvestmentAccount(self.valid_account_number, self.valid_client_number, self.valid_balance, ten_years_ago)
        expected_charge = InvestmentAccount.BASE_SERVICE_CHARGE  # $2.50
        actual_charge = account.get_service_charges()
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_get_service_charges_within_ten_years(self):
        """Test get_service_charges when date created is within the last 10 years."""
        recent_date = date.today() - timedelta(days=365 * 5)  # Within 10 years
        account = InvestmentAccount(self.valid_account_number, self.valid_client_number, self.valid_balance, recent_date, self.valid_management_fee)
        expected_charge = InvestmentAccount.BASE_SERVICE_CHARGE + self.valid_management_fee  # $2.50 + $2.00
        actual_charge = account.get_service_charges()
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_str_more_than_ten_years(self):
        """Test __str__ when date created is more than 10 years ago."""
        old_date = date.today() - timedelta(days=365 * 11)  # More than 10 years ago
        account = InvestmentAccount(self.valid_account_number, self.valid_client_number, self.valid_balance, old_date)
        expected_str = (f"<InvestmentAccount Management Fee: Waived "
                        f"Account Type: Investment>")
        self.assertEqual(str(account), expected_str)

    def test_str_within_ten_years(self):
        """Test __str__ when date created is within the last 10 years."""
        recent_date = date.today() - timedelta(days=365 * 5)  # Within 10 years
        account = InvestmentAccount(self.valid_account_number, self.valid_client_number, self.valid_balance, recent_date, self.valid_management_fee)
        expected_str = (f"<InvestmentAccount Management Fee: ${self.valid_management_fee:.2f} "
                        f"Account Type: Investment>")
        self.assertEqual(str(account), expected_str)

if __name__ == '__main__':
    unittest.main()


