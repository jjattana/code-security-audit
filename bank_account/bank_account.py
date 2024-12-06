"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from abc import ABC, abstractmethod
from datetime import date
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from patterns.observer.subject import Subject

class BankAccount(Subject, ABC):
    """
    Abstract base class for a bank account.
    Cannot be instantiated directly. Subclasses must use a ServiceChargeStrategy for calculating service charges.

    Attributes:
        LOW_BALANCE_LEVEL (float): The threshold below which a balance is considered low.
        LARGE_TRANSACTION_THRESHOLD (float): The threshold for large transactions that will trigger notifications.
    """
    LOW_BALANCE_LEVEL = 50.00
    LARGE_TRANSACTION_THRESHOLD = 10000.00
    
    def __init__(self, account_number, client_number, account_holder, balance, service_charge_strategy: ServiceChargeStrategy, date_created=None):
        """
        Initializes a BankAccount object with the common attributes and a service charge strategy.

        Args:
            account_number (int): The account number of the bank account.
            client_number (int): The client number associated with the account.
            account_holder (str): The name of the account holder.
            balance (float): The balance of the bank account.
            service_charge_strategy (ServiceChargeStrategy): A ServiceChargeStrategy instance for calculating service charges.
            date_created (date, optional): The date the account was created (defaults to today's date if not provided).
        
        Returns:
            None

        Raises:
            TypeError: If `date_created` is not of type `date`.
        """
        super().__init__()   # Initialize subject
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

        Args:
            None
        
        Returns:
            float: The calculated service charges based on the strategy.
        
        Raises:
            None
        """
        return self.service_charge_strategy.calculate_service_charges(self)
    
    def update_balance(self, amount):
        """
        Update the balance of the account by the specified amount.

        Args:
            amount (float): The amount to add to the balance (positive for deposit, negative for withdrawal).
        
        Returns:
            None
        
        Raises:
            None
        """
        self.balance += amount

        # Check for low balance
        if self.balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.balance:.2f}: on account {self.account_number}.")

        # Check for large transaction
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${amount:.2f}: on account {self.account_number}.")

    def deposit(self, amount):
        """
        Deposit the given amount into the bank account.

        Args:
            amount (float): The amount to deposit.
        
        Returns:
            None
        
        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        """
        Withdraw the given amount from the bank account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw.
        
        Returns:
            None
        
        Raises:
            ValueError: If the withdrawal amount is not positive or if there are insufficient funds.
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

        Args:
            None
        
        Returns:
            float: The current balance of the account.
        
        Raises:
            None
        """
        return self.balance

    def get_account_info(self):
        """
        Return a dictionary containing account details.

        Args:
            None
        
        Returns:
            dict: A dictionary with account details including account number, client number, 
                  account holder name, balance, and date created.
        
        Raises:
            None
        """
        return {
            'account_number': self.account_number,
            'client_number': self.client_number,
            'account_holder': self.account_holder,
            'balance': self.balance,
            'date_created': self._date_created
        }



