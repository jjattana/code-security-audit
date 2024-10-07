"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from datetime import date
from bank_account.bank_account import BankAccount  

# Base service charge amount
class ChequingAccount(BankAccount):
    """
    A class representing a Chequing Account, which extends the BankAccount class.

    Attributes:
        BASE_SERVICE_CHARGE (float): The base service charge for the account.
        overdraft_limit (float): The maximum overdraft limit for the account.
        overdraft_rate (float): The interest rate applied to the overdraft.
        date_created (date): The date the account was created.

    Methods:
        get_service_charges(): Calculates service charges based on the current balance.
        __str__(): Returns a string representation of the ChequingAccount object.
    """
    BASE_SERVICE_CHARGE = 0.50 

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
        # Initialize the superclass
        super().__init__(account_number, client_number, account_holder, initial_balance)

        # Validate overdraft_limit
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.__overdraft_limit = 1000.0

        # Validate overdraft_rate
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self.__overdraft_rate = 0.05

        # Validate date_created
        if date_created is None:
            self.__date_created = date.today()
        elif isinstance(date_created, str):
            try:
                year, month, day = map(int, date_created.split('-'))
                self.__date_created = date(year, month, day)  # Convert string to date
            except ValueError:
                self.__date_created = date.today()  # Default to today if invalid
        elif isinstance(date_created, date):
            self.__date_created = date_created
        else:
            self.__date_created = date.today()  # Default to today for other types

    @property
    def overdraft_limit(self):
        """Returns the overdraft limit for the account."""
        return self.__overdraft_limit

    @property
    def overdraft_rate(self):
        """Returns the overdraft interest rate for the account."""
        return self.__overdraft_rate

    @property
    def date_created(self):
        """Returns the date when the account was created."""
        return self.__date_created

    def __str__(self):
        """Returns a string representation of the ChequingAccount object."""
        return (f"Account Number: {self.account_number}\n"
                f"Client Number: {self.client_number}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:.2f}\n"
                f"Overdraft Rate: {self.__overdraft_rate * 100:.2f}%\n"
                f"Date Created: {self.__date_created.strftime('%Y-%m-%d')}\n"
                f"Account Type: Chequing")

    def get_service_charges(self):
        """Calculate the service charges based on the current balance and overdraft limit.

        Returns:
            float: The calculated service charge.
        """
        if self.balance >= self.overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            overdraft_amount = self.overdraft_limit - self.balance 
            service_charge = self.BASE_SERVICE_CHARGE + (overdraft_amount * self.overdraft_rate)
            return service_charge
