"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.minimun_balance_strategy import MinimumBalanceStrategy 

class SavingsAccount(BankAccount):
    """Class representing a savings account, inheriting from BankAccount."""

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float):
        """Initialize a SavingsAccount instance.

        Args:
            account_number (int): The unique identifier for the account.
            client_number (int): The unique identifier for the client.
            balance (float): The initial balance of the account.
            date_created (date): The date the account was created.
            minimum_balance (float): The minimum balance required to avoid extra service charges.
        """
        super().__init__(account_number, client_number, balance, date_created)
        
        self.balance = float(balance)  # Ensure balance is a float

        # Define a private attribute for MinimumBalanceStrategy
        self.__minimum_balance_strategy = MinimumBalanceStrategy(minimum_balance)

    def get_service_charges(self) -> float:
        """Calculate the service charges for the account.

        Returns:
            float: The calculated service charge.
        """
        return self.__minimum_balance_strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        """Return a string representation of the SavingsAccount.

        Returns:
            str: Detailed information about the SavingsAccount, including account number, balance, 
                  minimum balance, and account type.
        """
        return (
            f"Account Number: {self.account_number} "
            f"Balance: ${self.balance:.2f}\n"  
            f"Minimum Balance: ${self.__minimum_balance_strategy._MinimumBalanceStrategy__minimum_balance:.2f} "
            f"Account Type: Savings"
        )
