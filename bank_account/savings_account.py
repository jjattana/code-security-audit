"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from datetime import date
from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """Class representing a savings account, inheriting from BankAccount."""
    
    SERVICE_CHARGE_PREMIUM = 2.00  # Premium multiplier for service charges when balance is below minimum

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
        try:
            self._minimum_balance = float(minimum_balance)  # Set minimum balance
        except ValueError:
            self._minimum_balance = 50.0  # Default minimum balance if conversion fails

    def get_service_charges(self) -> float:
        """Calculate the service charges for the account.

        If the balance is above the minimum balance, a lower service charge is applied.
        If the balance is below the minimum, a premium service charge is applied.

        Returns:
            float: The calculated service charge.
        """
        if self.balance >= self._minimum_balance:
            return 0.50  # Standard service charge
        else:
            return 0.50 * self.SERVICE_CHARGE_PREMIUM  # Premium service charge

    def __str__(self) -> str:
        """Return a string representation of the SavingsAccount.

        Returns:
            str: Detailed information about the SavingsAccount, including account number, balance, 
                  minimum balance, and account type.
        """
        return (
            f"Account Number: {self.account_number} "
            f"Balance: ${self.balance:.2f}\n"  
            f"Minimum Balance: ${self._minimum_balance:.2f} Account Type: Savings"
        )



