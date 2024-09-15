"""
Description:
Author: Jashanpreet Kaur Jattana
"""

class BankAccount:
    def __init__(self, account_number: int, client_number: int, balance: float):
        # Validate account_number
        if type(account_number) is not int:
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number
        
        # Validate client_number
        if type(client_number) is not int:
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number
        
        # Validate balance
        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0.0

    # Property for account_number
    @property
    def account_number(self) -> int:
        """
        Gets account number of the bank account
        :return:
            int: account number of the bank account
        """
        return self.__account_number

    # Property for client_number
    @property
    def client_number(self) -> int:
        """
        Gets the client number of the bank account
        :return:
            int: client number of the bank account
        """
        return self.__client_number

    # Property for balance
    @property
    def balance(self) -> float:
        """
        Gets the current balance of the bank account
        :return:
            float: current balance of the bank account
        """
        return self.__balance

    # Update balance method
    def update_balance(self, amount: float) -> None:
        """
        Updates balance by adding the given amount
        """
        self.__balance += float(amount)
        

    # Deposit method
    def deposit(self, amount: float) -> None:
        """
        Deposits given amount into the bank account

        amount: float

        Raises 
        ValueError: If the deposit amount is not float or negative
        """
        if type(amount) not in (int, float):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)

    # Withdraw method
    def withdraw(self, amount: float) -> None:
        """
        Withddraws the given amount from the bank account

        amount: float

        Raises
        ValueError: If the withdrawl amount is not float, negative or more than the current balance,
        """
        if type(amount) not in (int, float):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")
        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance: ${self.__balance:,.2f}")
        
        self.update_balance(-amount)

    # String representation method
    def __str__(self) -> str:
        """
        Returns account number and current balance as a string reprentation
        :returns: 
            str: containing bank balance and account number
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}"


