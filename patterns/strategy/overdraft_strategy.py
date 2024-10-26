from service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account):
        """
        Calculate service charges based on the overdraft limit and rate.
        This logic is based on the original get_service_charges method 
        from the ChequingAccount class.
        """
        if account.balance < self.__overdraft_limit:
            overdraft_amount = self.__overdraft_limit - account.balance
            overdraft_fee = overdraft_amount * self.__overdraft_rate
            return self.BASE_SERVICE_CHARGE + overdraft_fee
        else:
            return self.BASE_SERVICE_CHARGE
