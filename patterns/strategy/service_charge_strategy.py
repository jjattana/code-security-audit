"""
Description:
Author: Jashanpreet Kaur Jattana
"""

from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    BASE_SERVICE_CHARGE = 5.0  # Example constant; set as needed

    @abstractmethod
    def calculate_service_charges(self, account):
        pass
