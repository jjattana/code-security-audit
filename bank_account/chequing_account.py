"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from datetime import date
from bank_account.bank_account import BankAccount  
from patterns.strategy.overdraft_strategy import OverdraftStrategy  # Import the OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    A class representing a Chequing Account, which extends the BankAccount class.This class includes additional
    functionality for managing overdrafts, such as setting overdraft limits and interest rates. The service charges 
    for this account type are calculated using the OverdraftStrategy.

    Attributes:
        BASE_SERVICE_CHARGE (float): The base service charge for the Chequing account.
        overdraft_limit (float): The maximum overdraft limit for the account.
        overdraft_rate (float): The interest rate applied to the overdraft balance.
        date_created (date): The date the account was created.
    """

    BASE_SERVICE_CHARGE = 0.50 

    def __init__(self, account_number, client_number, account_holder, initial_balance=500.0, overdraft_limit=1000, overdraft_rate=0.05, date_created=None):
        """
        Initializes a new ChequingAccount instance.

        Args:
            account_number (str): The account number.
            client_number (str): The client number.
            account_holder (str): The name of the account holder.
            initial_balance (float): The initial balance of the account. Defaults to 500.0.
            overdraft_limit (float): The maximum overdraft limit for the account. Defaults to 1000.0.
            overdraft_rate (float): The interest rate for the overdraft. Defaults to 0.05.
            date_created (date or str): The date the account was created. Can be a date object or a string in 'YYYY-MM-DD' format. Defaults to today if None.

        Returns:
            None

        Raises:
            ValueError: If the overdraft_limit or overdraft_rate is invalid or cannot be converted to float.
        """
        # Validate and set overdraft_limit
        try:
            overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            overdraft_limit = 1000.0

        # Validate and set overdraft_rate
        try:
            overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            overdraft_rate = 0.05

        # Create an OverdraftStrategy instance
        overdraft_strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

        # Initialize the superclass with service_charge_strategy
        super().__init__(account_number, client_number, account_holder, initial_balance, overdraft_strategy)

        # Set additional attributes
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

        # Validate and set date_created
        if date_created is None:
            self.__date_created = date.today()
        elif isinstance(date_created, str):
            try:
                year, month, day = map(int, date_created.split('-'))
                self.__date_created = date(year, month, day)
            except ValueError:
                self.__date_created = date.today()
        elif isinstance(date_created, date):
            self.__date_created = date_created
        else:
            self.__date_created = date.today()

    @property
    def overdraft_limit(self):
        """
        Returns the overdraft limit for the account.
        
        Args:
            None

        Returns:
            float: The overdraft limit for the account.
        """
        return self.__overdraft_limit

    @property
    def overdraft_rate(self):
        """
        Returns the overdraft interest rate for the account.
        
        Args:
            None

        Returns:
            float: The overdraft interest rate for the account.
        """
        return self.__overdraft_rate

    @property
    def date_created(self):
        """
        Returns the date when the account was created.
        
        Args:
            None

        Returns:
            date: The date when the account was created.
        """
        return self.__date_created

    def __str__(self):
        """
        Returns a string representation of the ChequingAccount object.
        
        Args:
            None

        Returns:
            str: A string representing the ChequingAccount instance with detailed account information.
        """
        return (f"Account Number: {self.account_number}\n"
                f"Client Number: {self.client_number}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:.2f}\n"
                f"Overdraft Rate: {self.__overdraft_rate * 100:.2f}%\n"
                f"Date Created: {self.__date_created.strftime('%Y-%m-%d')}\n"
                f"Account Type: Chequing")

    def get_service_charges(self):
        """
        Calculate the service charges using the OverdraftStrategy instance.
        
        Args:
            None

        Returns:
            float: The calculated service charges based on the overdraft limit and rate.
        """
        return self.__overdraft_strategy.calculate_service_charges(self)
