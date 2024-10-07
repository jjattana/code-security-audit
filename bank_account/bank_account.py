"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from abc import ABC, abstractmethod
from datetime import date

class BankAccount(ABC):
    """
    Abstract base class for a bank account.
    Cannot be instantiated directly. Subclasses must implement the get_service_charges method.
    """
    
    def __init__(self, account_number, client_number, account_holder, balance, date_created=None):
        """
        Initializes a BankAccount object with the common attributes.

        :param account_number: The account number of the bank account
        :param account_holder: The name of the account holder
        :param balance: The balance of the bank account
        :param date_created: The date the account was created (defaults to today's date if not provided)
        """
        self.account_number = account_number
        self.client_number = client_number
        self.account_holder = account_holder
        self.balance = balance
        
        # Validate the date_created argument. If not a date, use today's date.
        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

    @abstractmethod
    def get_service_charges(self):
        """
        Abstract method to calculate and return the service charges for the bank account.
        Must be implemented by subclasses.
        """
        pass

    def deposit(self, amount):
        """
        Deposit the given amount into the bank account.

        :param amount: The amount to deposit
        """
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        """
        Withdraw the given amount from the bank account if sufficient funds are available.

        :param amount: The amount to withdraw
        """
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise ValueError("Insufficient funds")
        else:
            raise ValueError("Withdrawal amount must be positive")

    def get_balance(self):
        """
        Return the current balance of the bank account.

        :return: The balance of the account
        """
        return self.balance

    def get_account_info(self):
        """
        Return a dictionary containing account details.

        :return: A dictionary with account details
        """
        return {
            'account_number': self.account_number,
            'client_number': self.client_number,
            'account_holder': self.account_holder,
            'balance': self.balance,
            'date_created': self._date_created
        }


class ChequingAccount(BankAccount):
    """
    Concrete subclass of BankAccount representing a chequing account.
    """

    def get_service_charges(self):
        """
        Return the service charges for the chequing account.

        Chequing accounts incur a 2% service charge.
        :return: The calculated service charges based on the account balance
        """
        return self.balance * 0.02  # Example: 2% service charge for chequing accounts


class SavingsAccount(BankAccount):
    """
    Concrete subclass of BankAccount representing a savings account.
    """

    def get_service_charges(self):
        """
        Return the service charges for the savings account.

        Savings accounts incur a 1% service charge.
        :return: The calculated service charges based on the account balance
        """
        return self.balance * 0.01  # Example: 1% service charge for savings accounts







