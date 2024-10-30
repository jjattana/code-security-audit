"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: Jashanpreet Kaur Jattana
Date: 2024-10-29
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from datetime import date
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from client.client import Client



# 2. Create a Client object with data of your choice.
client_data1 = Client(client_number=105, first_name="Rohit", last_name="Sharma", email_address="rsharma@pixell-river.com")



# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing_account = ChequingAccount(account_number= 67890, client_number= client_data1.client_number, initial_balance= 1500.0)
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
savings_account = SavingsAccount(account_number=12345, client_number=client_data1.client_number, balance= 2000.0)





# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
chequing_account.attach(client_data1)
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
savings_account.attach(client_data1)





# 5a. Create a second Client object with data of your choice.
client_data2 = Client(client_number=106, first_name="Jashanpreet", last_name="Jattana", email_address="jjattana@pixell-river.com")
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
savings_account2 = SavingsAccount(account_number= 57684, client_number=client_data2.client_number, balance = 1000.0)
savings_account2.attach(client_data2)



# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

# 6. Perform transactions on ChequingAccount and SavingsAccount objects

# Transactions for the ChequingAccount
try:
    # Deposit that does not trigger notification
    chequing_account.deposit(500)
    print("Deposited $500 into ChequingAccount.")
except Exception as e:
    print("Error during deposit into ChequingAccount:", e)

try:
    # Large withdrawal that triggers notification (assuming threshold is set, e.g., $1000)
    chequing_account.withdraw(1200)
    print("Withdrew $1200 from ChequingAccount.")
except Exception as e:
    print("Error during withdrawal from ChequingAccount:", e)

try:
    # Withdrawal that causes low balance notification (assuming balance threshold, e.g., $100)
    chequing_account.withdraw(700)
    print("Withdrew $700 from ChequingAccount.")
except Exception as e:
    print("Error during withdrawal from ChequingAccount:", e)

# Transactions for the first SavingsAccount
try:
    # Deposit that does not trigger notification
    savings_account.deposit(300)
    print("Deposited $300 into SavingsAccount.")
except Exception as e:
    print("Error during deposit into SavingsAccount:", e)

try:
    # Large deposit that triggers notification
    savings_account.deposit(2000)
    print("Deposited $2000 into SavingsAccount.")
except Exception as e:
    print("Error during deposit into SavingsAccount:", e)

try:
    # Withdrawal that causes low balance notification
    savings_account.withdraw(2500)
    print("Withdrew $2500 from SavingsAccount.")
except Exception as e:
    print("Error during withdrawal from SavingsAccount:", e)

# Transactions for the second SavingsAccount (savings_account2)
try:
    # Deposit that does not trigger notification
    savings_account2.deposit(200)
    print("Deposited $200 into second SavingsAccount.")
except Exception as e:
    print("Error during deposit into second SavingsAccount:", e)

try:
    # Large transaction that triggers notification
    savings_account2.deposit(1500)
    print("Deposited $1500 into second SavingsAccount.")
except Exception as e:
    print("Error during large deposit into second SavingsAccount:", e)

try:
    # Small withdrawal that does not trigger notification
    savings_account2.withdraw(300)
    print("Withdrew $300 from second SavingsAccount.")
except Exception as e:
    print("Error during withdrawal from second SavingsAccount:", e)
