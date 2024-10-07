"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from datetime import date
from bank_account.bank_account import BankAccount  

 # Base service charge amount

class ChequingAccount(BankAccount):
    BASE_SERVICE_CHARGE = 0.50 

    def __init__(self, account_number, client_number, account_holder, initial_balance=0.0, overdraft_limit=-100, overdraft_rate=0.05, date_created=None):
        # Initialize the superclass
        super().__init__(account_number, client_number, account_holder, initial_balance)

        # Validate overdraft_limit
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.__overdraft_limit = -100.0

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
                self.__date_created = date.today()  # default to today if invalid
        elif isinstance(date_created, date):
            self.__date_created = date_created
        else:
            self.__date_created = date.today()  # default to today for other types

    @property
    def overdraft_limit(self):
        return self.__overdraft_limit

    @property
    def overdraft_rate(self):
        return self.__overdraft_rate

    @property
    def date_created(self):
        return self.__date_created

    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Client Number: {self.client_number}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:.2f}\n"
                f"Overdraft Rate: {self.__overdraft_rate * 100:.2f}%\n"
                f"Date Created: {self.__date_created.strftime('%Y-%m-%d')}\n"
                f"Account Type: Chequing")

    def get_service_charges(self):
        """Calculate the service charges based on balance and overdraft limit."""
        if self.balance >= self.overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            overdraft_amount = self.overdraft_limit - self.balance  # Should give a positive value
            service_charge = self.BASE_SERVICE_CHARGE + (overdraft_amount * self.overdraft_rate)
            return service_charge