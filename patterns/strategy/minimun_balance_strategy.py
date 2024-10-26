from service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance: float):
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account):
        """
        Calculate service charges based on the account balance and minimum balance.
        """
        if account.balance < self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE + self.SERVICE_CHARGE_PREMIUM
        else:
            return self.BASE_SERVICE_CHARGE
