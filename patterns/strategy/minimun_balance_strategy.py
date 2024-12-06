"""
Description:
Author: Jashanpreet Kaur Jattana
"""
from .service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Concrete implementation of ServiceChargeStrategy for calculating service charges
    based on a minimum balance requirement.

    Attributes:
        SERVICE_CHARGE_PREMIUM (float): Additional service charge applied if the account
                                         balance falls below the minimum balance.
        __minimum_balance (float): The minimum balance that must be maintained in the account.
    """
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance: float):
        """
        Initializes the MinimumBalanceStrategy with a specified minimum balance.

        Args:
            minimum_balance (float): The minimum balance that must be maintained in the account
                                     to avoid additional service charges.
        """
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account):
        """
        Calculate service charges based on the account balance and minimum balance.

        Args:
            account: The bank account object for which service charges are to be calculated.

        Returns:
            float: The calculated service charges based on whether the account balance
                   is below the minimum balance.
        """
        if account.balance < self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE + self.SERVICE_CHARGE_PREMIUM
        else:
            return self.BASE_SERVICE_CHARGE
