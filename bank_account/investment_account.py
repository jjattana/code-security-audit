"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy  

class InvestmentAccount(BankAccount):
    """
    A class representing an Investment Account, which extends the BankAccount class.
    """

    def __init__(self, account_number: int, client_number: int, account_holder: str, balance: float, date_created: date, management_fee: float = 0.0):
        """
        Initializes an InvestmentAccount object.

        Args:
            account_number (int): The account number.
            client_number (int): The client number associated with the account.
            account_holder (str): The name of the account holder.
            balance (float): The initial balance of the account.
            date_created (date): The date the account was created.
            management_fee (float, optional): The management fee for the account. Default is 0.0.
        """
        super().__init__(account_number, client_number, account_holder, balance, date_created)
        
        # Initialize ManagementFeeStrategy for service charge calculations
        self._service_charge_strategy = ManagementFeeStrategy(management_fee, date_created)

    def get_service_charges(self):
        """
        Calculate service charges using the ManagementFeeStrategy.

        :return: The calculated service charge
        """
        return self._service_charge_strategy.calculate_service_charges(self.balance)

    def __str__(self):
        """Returns a string representation of the InvestmentAccount object."""
        return (f"Account Number: {self.account_number}\n"
                f"Client Number: {self.client_number}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"Account Type: Investment")
