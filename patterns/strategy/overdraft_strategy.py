"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from service_charge_strategy import ServiceChargeStrategy


class OverdraftStrategy(ServiceChargeStrategy):
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        # Private attributes based on the diagram's visibility notation
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account):
        """
        Calculates the service charges for an account based on the overdraft strategy.
        Uses the same logic as the get_service_charges method in the ChequingAccount class.
        """
        service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE
        if account.balance < 0:
            overdraft_amount = max(0, -account.balance - self.__overdraft_limit)
            service_charge += overdraft_amount * self.__overdraft_rate
        return service_charge
