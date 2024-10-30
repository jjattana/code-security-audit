"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account):
        """
        Calculate service charges based on the management fee.
        """
        if self.__date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE + self.__management_fee
        else:
            return self.BASE_SERVICE_CHARGE
