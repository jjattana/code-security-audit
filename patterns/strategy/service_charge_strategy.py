from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account):
        """Calculates the service charges for a given account.
        Must be implemented by subclasses."""
        pass
