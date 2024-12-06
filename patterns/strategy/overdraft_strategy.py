"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from .service_charge_strategy import ServiceChargeStrategy


class OverdraftStrategy(ServiceChargeStrategy):
    """
    Concrete implementation of ServiceChargeStrategy for calculating service charges
    based on an overdraft limit and rate.

    Attributes:
        __overdraft_limit (float): The maximum amount that can be overdrafted.
        __overdraft_rate (float): The rate applied to the overdrafted amount.
    """
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the OverdraftStrategy with a specified overdraft limit and rate.

        Args:
            overdraft_limit (float): The limit for overdraft, below which service charges apply.
            overdraft_rate (float): The rate at which service charges are calculated for the overdraft amount.
        """
        # Private attributes based on the diagram's visibility notation
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account):
        """
        Calculates the service charges for an account based on the overdraft strategy.
        Uses the same logic as the get_service_charges method in the ChequingAccount class.

        Args:
            account: The bank account object for which service charges are to be calculated.

        Returns:
            float: The calculated service charges based on the account balance and overdraft conditions.
        """
        service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE
        if account.balance < 0:
            overdraft_amount = max(0, -account.balance - self.__overdraft_limit)
            service_charge += overdraft_amount * self.__overdraft_rate
        return service_charge
