"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date 

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account = None
try:
    chequing_account = ChequingAccount(account_number=12345, client_number=67890, initial_balance=500.0, account_holder="Jashanpreet Jattana", date_created=date.today(), overdraft_limit=1000.0)
except Exception as e:
    print(f"Error creating ChequingAccount: {e}")

# 3. Print the ChequingAccount created in step 2.
print(chequing_account)
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    print(f"Service Charges: {chequing_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges: {e}")


# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
try:
    chequing_account.deposit(1500.0)  
except Exception as e:
    print(f"Error depositing into ChequingAccount: {e}")
# 4b. Print the ChequingAccount
print(chequing_account)
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    print(f"Service Charges after deposit: {chequing_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges after deposit: {e}")


print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings_account = None
try:
    savings_account = SavingsAccount(account_number=12345, client_number=67890, balance=1000.0, date_created=date.today(), minimum_balance=500.0)
except Exception as e:
    print(f"Error creating SavingsAccount: {e}")


# 6. Print the SavingsAccount created in step 5.
print(savings_account)
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    print(f"Service Charges: {savings_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges: {e}")



# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
try:
    savings_account.withdraw(600.0)  
except Exception as e:
    print(f"Error withdrawing from SavingsAccount: {e}")
# 7b. Print the SavingsAccount.
print(savings_account)
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    print(f"Service Charges after withdrawal: {savings_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges after withdrawal: {e}")



print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_account = None
try:
    investment_account = InvestmentAccount(account_number=98765, client_number=67890, balance=2000.0, date_created=date(2022, 5, 10))  
except Exception as e:
    print(f"Error creating InvestmentAccount (recent): {e}")


# 9a. Print the InvestmentAccount created in step 8.
print(investment_account)
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
try:
    print(f"Service Charges: {investment_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges: {e}")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_account_old = None
try:
    investment_account_old = InvestmentAccount(account_number=87654, client_number=67890, balance=1500.0, date_created=date(2010, 3, 15))  # Date prior to 10 years ago
except Exception as e:
    print(f"Error creating InvestmentAccount (old): {e}")


# 11a. Print the InvestmentAccount created in step 10.
print(investment_account_old)
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
try:
    print(f"Service Charges: {investment_account_old.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges: {e}")


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    chequing_account.withdraw(chequing_account.get_service_charges())
    savings_account.withdraw(savings_account.get_service_charges())
    investment_account.withdraw(investment_account.get_service_charges())
    investment_account_old.withdraw(investment_account_old.get_service_charges())
except Exception as e:
    print(f"Error updating balances: {e}")



# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequing_account)
print(savings_account)
print(investment_account)
print(investment_account_old)
