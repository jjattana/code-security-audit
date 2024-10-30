"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Concrete implementation of ServiceChargeStrategy for calculating service charges
    based on a management fee and the age of the account.

    Attributes:
        TEN_YEARS_AGO (date): A constant date representing the date ten years prior to today.
        __date_created (date): The date when the account was created.
        __management_fee (float): The management fee charged if the account is older than ten years.
    """
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes the ManagementFeeStrategy with the account creation date and management fee.

        Args:
            date_created (date): The date when the account was created.
            management_fee (float): The management fee to be applied if the account is older
                                    than ten years.
        """
        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account):
        """
        Calculate service charges based on the management fee.

        Args:
            account: The bank account object for which service charges are to be calculated.

        Returns:
            float: The calculated service charges based on whether the account age exceeds ten years.
        """
        if self.__date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE + self.__management_fee
        else:
            return self.BASE_SERVICE_CHARGE
