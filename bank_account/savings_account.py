"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from datetime import date
from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    SERVICE_CHARGE_PREMIUM = 2.00

    def __init__(self, account_number, client_number, balance, date_created, minimum_balance):
        super().__init__(account_number, client_number, balance, date_created)
        
        self.balance = float(balance)  
        try:
            self._minimum_balance = float(minimum_balance)
        except ValueError:
            self._minimum_balance = 50.0  

    def get_service_charges(self):
        if self.balance >= self._minimum_balance:
            return 0.50  
        else:
            return 0.50 * self.SERVICE_CHARGE_PREMIUM  

    def __str__(self):
        return (
            f"Account Number: {self.account_number} "
            f"Balance: ${self.balance:.2f}\n"  
            f"Minimum Balance: ${self._minimum_balance:.2f} Account Type: Savings"
        )


