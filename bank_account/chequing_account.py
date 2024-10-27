"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from patterns.strategy.overdraft_strategy import OverdraftStrategy  

class ChequingAccount(BankAccount):
    """
    A class representing a Chequing Account, which extends the BankAccount class.
    """

    def __init__(self, account_number, client_number, account_holder, initial_balance=500.0, overdraft_limit=1000, overdraft_rate=0.05, date_created=None):
        """
        Initializes a new ChequingAccount instance.

        Parameters:
            account_number (str): The account number.
            client_number (str): The client number.
            account_holder (str): The name of the account holder.
            initial_balance (float): The initial balance of the account. Defaults to 500.0.
            overdraft_limit (float): The maximum overdraft limit for the account. Defaults to 1000.0.
            overdraft_rate (float): The interest rate for the overdraft. Defaults to 0.05.
            date_created (date or str): The date the account was created. Can be a date object or a string in 'YYYY-MM-DD' format. Defaults to today if None.
        """
        super().__init__(account_number, client_number, account_holder, initial_balance, date_created)

        # Define a new private attribute for overdraft strategy with appropriate arguments
        self._overdraft_strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

    def get_service_charges(self):
        """
        Calculate service charges using the overdraft strategy.

        :return: The calculated service charge
        """
        return self._overdraft_strategy.calculate_service_charges(self.balance)

    def __str__(self):
        """Returns a string representation of the ChequingAccount object."""
        return (f"Account Number: {self.account_number}\n"
                f"Client Number: {self.client_number}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"Account Type: Chequing")
