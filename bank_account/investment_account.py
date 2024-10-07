"""
Description: 
Author: Jashanpreet Kaur Jattana
"""

from datetime import date
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    BASE_SERVICE_CHARGE = 2.50  
    MANAGEMENT_FEE = 0.50        
    WAIVED_FEE = 0               

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, management_fee: float = WAIVED_FEE):
        self._balance = float(balance)
        self._date_created = date_created
        if not isinstance(management_fee, (int, float)) or management_fee < 0:
            raise ValueError("Management fee cannot be negative.")
        
        super().__init__(account_number, client_number, self._balance, self._date_created)  
        
        self.management_fee = management_fee  

    @property
    def date_created(self):
        return self._date_created

    def get_service_charges(self) -> float:
        """
        Calculate the service charges based on the account age and management fee.
        """
        account_age_years = self.calculate_account_age()

        if account_age_years < 10:
            return self.BASE_SERVICE_CHARGE + self.management_fee  
        elif account_age_years == 10:
            return self.BASE_SERVICE_CHARGE  
        else:  
            return self.BASE_SERVICE_CHARGE + self.MANAGEMENT_FEE  

    def calculate_account_age(self):
        age = (date.today() - self._date_created).days // 365
        return age

    def __str__(self) -> str:
        """
        String representation of the InvestmentAccount object.
        """
        if self.management_fee == self.WAIVED_FEE:
            fee_status = "Waived"
        else:
            fee_status = f"${self.management_fee:.2f}"  

        return (f"<{self.__class__.__name__} "
                f"Management Fee: {fee_status} "
                f"Account Type: Investment>")

