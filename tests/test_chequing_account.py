"""
Description:
Author: Jashanpreet Kaur Jattana
"""


import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount  

class TestChequingAccount(unittest.TestCase):

    def test_init_valid_attributes(self):
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", initial_balance=500.00, 
                                   overdraft_limit=1000.00, overdraft_rate=0.05, date_created="2023-01-01")
        self.assertEqual(account.account_number, 12345)
        self.assertEqual(account.client_number, 67890)
        self.assertEqual(account.account_holder, "Jashanpreet Jattana")
        self.assertEqual(account.balance, 500.00)
        self.assertEqual(account.overdraft_limit, 1000.00)
        self.assertEqual(account.overdraft_rate, 0.05)
        self.assertEqual(account.date_created.strftime('%Y-%m-%d'), "2023-01-01")

    def test_init_invalid_overdraft_limit(self):
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", initial_balance=500.00, 
                                   overdraft_limit="invalid", overdraft_rate=0.05, date_created="2023-01-01")
        self.assertEqual(account.overdraft_limit, 1000.00)

    def test_init_invalid_overdraft_rate(self):
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", initial_balance=500.00, 
                                   overdraft_limit=1000.00, overdraft_rate="invalid", date_created="2023-01-01")
        self.assertEqual(account.overdraft_rate, 0.05)

    def test_init_invalid_date_created(self):
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", initial_balance=500.00, 
                                   overdraft_limit=1000.00, overdraft_rate=0.05, date_created=123456)
        self.assertEqual(account.date_created.strftime('%Y-%m-%d'), date.today().strftime('%Y-%m-%d'))

    def test_get_service_charges_balance_greater_than_limit(self):
        account = ChequingAccount(account_number=1234567, client_number=67890, account_holder="Jashanpreet Jattana", initial_balance=1500.00, 
                                   overdraft_limit=1000.00, overdraft_rate=0.05)
        expected_charge = 0.50
        actual_charge = account.get_service_charges()
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_get_service_charges_balance_less_than_limit(self):
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", initial_balance=500.00, 
                                   overdraft_limit=1000.00, overdraft_rate=0.05)
        expected_charge = 0.50 + (1000.00 - (500.00)) * 0.05  # Calculated based on formula
        actual_charge = account.get_service_charges()
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_get_service_charges_balance_equal_to_limit(self):
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", initial_balance=1000.00, 
                                   overdraft_limit=1000.00, overdraft_rate=0.05)
        expected_charge = 0.50
        actual_charge = account.get_service_charges()
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_str_method(self):   
        account = ChequingAccount(account_number=12345, client_number=67890, account_holder="Jashanpreet Jattana", initial_balance=500.00, 
                                   overdraft_limit=1000.00, overdraft_rate=0.05, date_created="2023-01-01")
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

