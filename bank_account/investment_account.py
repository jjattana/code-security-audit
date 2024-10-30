"""
Description: 
Author: Jashanpreet Kaur Jattana
"""

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy  

class InvestmentAccount(BankAccount):
    """Represents an investment account, inheriting from BankAccount.

    Attributes:
        BASE_SERVICE_CHARGE (float): The base service charge for the account.
        MANAGEMENT_FEE (float): The standard management fee for the account.
        WAIVED_FEE (float): The waived fee status for the management fee.
    """
    
    BASE_SERVICE_CHARGE = 2.50  
    MANAGEMENT_FEE = 0.50        
    WAIVED_FEE = 0               

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, management_fee: float = WAIVED_FEE):
        """Initializes an InvestmentAccount object.

        Args:
            account_number (int): The account number.
            client_number (int): The client number associated with the account.
            balance (float): The initial balance of the account.
            date_created (date): The date the account was created.
            management_fee (float, optional): The management fee for the account. Default is WAIVED_FEE.

        Raises:
            ValueError: If the management fee is negative.
        """
        self._balance = float(balance)
        self._date_created = date_created
        
        if not isinstance(management_fee, (int, float)) or management_fee < 0:
            raise ValueError("Management fee cannot be negative.")
        
        super().__init__(account_number, client_number, self._balance, self._date_created)

        self.management_fee = management_fee  

        # Define a private attribute for ManagementFeeStrategy
        self.__management_fee_strategy = ManagementFeeStrategy(date_created, management_fee)

    @property
    def date_created(self):
        """Returns the date the account was created."""
        return self._date_created

    def get_service_charges(self) -> float:
        """Calculate the service charges using ManagementFeeStrategy.

        Returns:
            float: The calculated service charges.
        """
        return self.__management_fee_strategy.calculate_service_charges(self)

    def calculate_account_age(self) -> int:
        """Calculates the age of the account in years.

        Returns:
            int: The age of the account in years.
        """
        age = (date.today() - self._date_created).days // 365
        return age

    def __str__(self) -> str:
        """String representation of the InvestmentAccount object.

        Returns:
            str: A string describing the InvestmentAccount instance, including the management fee status.
        """
        if self.management_fee == self.WAIVED_FEE:
            fee_status = "Waived"
        else:
            fee_status = f"${self.management_fee:.2f}"  

        return (f"<{self.__class__.__name__} "
                f"Management Fee: {fee_status} "
                f"Account Type: Investment>")
