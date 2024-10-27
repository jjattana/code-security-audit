"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from abc import ABC, abstractmethod
from datetime import date
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy  

class BankAccount(ABC):
    """
    Abstract base class for a bank account.
    Cannot be instantiated directly. Subclasses must implement the get_service_charges method.
    """

    def __init__(self, account_number, client_number, account_holder, balance, date_created=None):
        """
        Initializes a BankAccount object with the common attributes.

        :param account_number: The account number of the bank account
        :param client_number: The client number of the account holder
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

        # Initialize service charge strategy 
        self._service_charge_strategy = None

    @abstractmethod
    def get_service_charges(self):
        """
        Calculate and return the service charges for the bank account using the assigned strategy.
        Must be implemented by subclasses.
        """
        if self._service_charge_strategy is None:
            raise NotImplementedError("Service charge strategy not set.")
        return self._service_charge_strategy.calculate_service_charges(self.balance)

    def set_service_charge_strategy(self, strategy: ServiceChargeStrategy):
        """
        Set the service charge strategy for this account.

        :param strategy: An instance of a ServiceChargeStrategy subclass
        """
        self._service_charge_strategy = strategy

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
