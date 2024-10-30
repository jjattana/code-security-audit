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
    Cannot be instantiated directly. Subclasses must use a ServiceChargeStrategy for calculating service charges.
    """
    
    def __init__(self, account_number, client_number, account_holder, balance, service_charge_strategy: ServiceChargeStrategy, date_created=None):
        """
        Initializes a BankAccount object with the common attributes and a service charge strategy.

        :param account_number: The account number of the bank account
        :param client_number: The client number associated with the account
        :param account_holder: The name of the account holder
        :param balance: The balance of the bank account
        :param service_charge_strategy: A ServiceChargeStrategy instance for calculating service charges
        :param date_created: The date the account was created (defaults to today's date if not provided)
        """
        self.account_number = account_number
        self.client_number = client_number
        self.account_holder = account_holder
        self.balance = balance
        self.service_charge_strategy = service_charge_strategy  # Using strategy pattern for service charges
        
        # Validate the date_created argument. 
        self._date_created = date_created if isinstance(date_created, date) else date.today()

    def get_service_charges(self):
        """
        Calculate and return the service charges using the associated ServiceChargeStrategy.

        :return: The calculated service charges
        """
        return self.service_charge_strategy.calculate_service_charges(self)

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

    def __init__(self, account_number, client_number, account_holder, balance, service_charge_strategy, date_created=None):
        super().__init__(account_number, client_number, account_holder, balance, service_charge_strategy, date_created)


class SavingsAccount(BankAccount):
    """
    Concrete subclass of BankAccount representing a savings account.
    """

    def __init__(self, account_number, client_number, account_holder, balance, service_charge_strategy, date_created=None):
        super().__init__(account_number, client_number, account_holder, balance, service_charge_strategy, date_created)
