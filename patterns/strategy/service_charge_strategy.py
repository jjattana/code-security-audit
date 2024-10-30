"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    Abstract base class for defining service charge strategies for bank accounts.

    Attributes:
        BASE_SERVICE_CHARGE (float): A constant representing the base service charge
                                      that can be used in derived classes.
    """
    BASE_SERVICE_CHARGE = 5.0  # Example constant; set as needed

    @abstractmethod
    def calculate_service_charges(self, account):
        """
        Calculate the service charges for a given bank account.

        Args:
            account: The bank account object for which service charges are to be calculated.

        Returns:
            float: The calculated service charges for the specified account.
        """
        pass
