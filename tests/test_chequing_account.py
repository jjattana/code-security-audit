"""
Description:
Author: Jashanpreet Kaur Jattana
"""


import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount  

class TestChequingAccount(unittest.TestCase):
    """Unit tests for the ChequingAccount class, ensuring proper initialization
    and functionality of methods."""

    def test_init_valid_attributes(self):
        """Test the initialization of ChequingAccount with valid attributes.
        
        This test checks that the account attributes are set correctly upon 
        instantiation.
        """
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", 
                                   initial_balance=500.00, overdraft_limit=1000.00, overdraft_rate=0.05, 
                                   date_created="2023-01-01")
        self.assertEqual(account.account_number, 12345)
        self.assertEqual(account.client_number, 67890)
        self.assertEqual(account.account_holder, "Jashanpreet Jattana")
        self.assertEqual(account.balance, 500.00)
        self.assertEqual(account.overdraft_limit, 1000.00)
        self.assertEqual(account.overdraft_rate, 0.05)
        self.assertEqual(account.date_created.strftime('%Y-%m-%d'), "2023-01-01")

    def test_init_invalid_overdraft_limit(self):
        """Test initialization of ChequingAccount with an invalid overdraft limit.
        
        This test ensures that an invalid overdraft limit results in the default value of 1000.0.
        """
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", 
                                   initial_balance=500.00, overdraft_limit="invalid", overdraft_rate=0.05, 
                                   date_created="2023-01-01")
        self.assertEqual(account.overdraft_limit, 1000.00)

    def test_init_invalid_overdraft_rate(self):
        """Test initialization of ChequingAccount with an invalid overdraft rate.
        
        This test checks that an invalid overdraft rate results in the default value of 0.05.
        """
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", 
                                   initial_balance=500.00, overdraft_limit=1000.00, overdraft_rate="invalid", 
                                   date_created="2023-01-01")
        self.assertEqual(account.overdraft_rate, 0.05)

    def test_init_invalid_date_created(self):
        """Test initialization of ChequingAccount with an invalid date created.
        
        This test ensures that an invalid date created results in today's date as the default.
        """
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", 
                                   initial_balance=500.00, overdraft_limit=1000.00, overdraft_rate=0.05, 
                                   date_created=123456)
        self.assertEqual(account.date_created.strftime('%Y-%m-%d'), date.today().strftime('%Y-%m-%d'))

    def test_get_service_charges_balance_greater_than_limit(self):
        """Test service charges when balance is greater than overdraft limit.
        
        This test checks that the service charge is the base amount when the balance exceeds the overdraft limit.
        """
        account = ChequingAccount(account_number=1234567, client_number=67890, account_holder="Jashanpreet Jattana", 
                                   initial_balance=1500.00, overdraft_limit=1000.00, overdraft_rate=0.05)
        expected_charge = 0.50
        actual_charge = account.get_service_charges()
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_get_service_charges_balance_less_than_limit(self):
        """Test service charges when balance is less than overdraft limit.
        
        This test verifies that the service charge is calculated correctly when the balance is below the overdraft limit.
        """
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", 
                                   initial_balance=500.00, overdraft_limit=1000.00, overdraft_rate=0.05)
        expected_charge = 0.50 + (1000.00 - 500.00) * 0.05  # Calculated based on formula
        actual_charge = account.get_service_charges()
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_get_service_charges_balance_equal_to_limit(self):
        """Test service charges when balance is equal to overdraft limit.
        
        This test ensures that the service charge is the base amount when the balance equals the overdraft limit.
        """
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", 
                                   initial_balance=1000.00, overdraft_limit=1000.00, overdraft_rate=0.05)
        expected_charge = 0.50
        actual_charge = account.get_service_charges()
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_str_method(self):   
        """Test the string representation of the ChequingAccount object.
        
        This test verifies that the __str__ method returns the expected string format with all account details.
        """
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", 
                                   initial_balance=500.00, overdraft_limit=1000.00, overdraft_rate=0.05, 
                                   date_created="2023-01-01")
        expected_str = ("Account Number: 12345\n"
                        "Client Number: 67890\n"
                        "Account Holder: Jashanpreet Jattana\n"
                        "Balance: $500.00\n"
                        "Overdraft Limit: $1000.00\n"
                        "Overdraft Rate: 5.00%\n"
                        "Date Created: 2023-01-01\n"
                        "Account Type: Chequing")
        self.assertEqual(str(account), expected_str)

if __name__ == '__main__':
    unittest.main()

