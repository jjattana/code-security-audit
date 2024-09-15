"""
Description:
Author: Jashanpreet Kaur Jattana
"""

class BankAccount:
    def __init__(self, account_number: int, client_number: int, balance: float):
        # Validate account_number
        if type(account_number) is not int:
            raise ValueError("Account number must be an integer.")
        self._account_number = account_number
        
        # Validate client_number
        if type(client_number) is not int:
            raise ValueError("Client number must be an integer.")
        self._client_number = client_number
        
        # Validate balance
        try:
            self._balance = float(balance)
        except ValueError:
            self._balance = 0.0

    # Property for account_number
    @property
    def account_number(self) -> int:
        return self._account_number

    # Property for client_number
    @property
    def client_number(self) -> int:
        return self._client_number

    # Property for balance
    @property
    def balance(self) -> float:
        return self._balance

    # Update balance method
    def update_balance(self, amount: float) -> None:
        self._balance += float(amount)
        

    # Deposit method
    def deposit(self, amount: float) -> None:
        # Type check without isinstance
        if type(amount) not in (int, float):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)

    # Withdraw method
    def withdraw(self, amount: float) -> None:
        # Type check without isinstance
        if type(amount) not in (int, float):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")
        if amount > self._balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance: ${self._balance:,.2f}")
        
        self.update_balance(-amount)

    # String representation method
    def __str__(self) -> str:
        return f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}"

# Example usage:
# account = BankAccount(12345, 67890, 500.0)
# print(account)
# account.deposit(200.0)
# print(account)
# account.withdraw(100.0)
# print(account)
