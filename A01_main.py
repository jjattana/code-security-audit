""""
Description: A client program written to verify correctness of 
the BankAccount and Transaction classes.
Author: ACE Faculty
Edited by: Jashanpreet Kaur Jattana
Date: 2024-09-14
"""
from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Transaction classes.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.
    try:
        client = Client(client_number=67890, first_name="Jashanpreet", last_name="Jattana", email_address="jjattana@pixell-river.com")  
    except Exception as e:
        print("Error creating Client instance:", e)



    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None
 

    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance. 
    if client:
        try:
            bank_account = BankAccount(account_number=12345, client_number=client.client_number, balance=500.0)
        except Exception as e:
            print("Error creating BankAccount instance:", e)



    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 
    if client:
        try:
            invalid_account = BankAccount(account_number=12345, client_number=client.client_number, balance="invalid_balance")
        except Exception as e:
            print("Error creating BankAccount with invalid balance:", e)


    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.
    if client:
        try:
            print(client)
        except Exception as e:
            print("Error printing Client instance:", e)
    if bank_account:
        try:
            print(bank_account)
        except Exception as e:
            print("Error printing BankAccount instance:", e)



    # 6. Attempt to deposit a non-numeric value into the BankAccount create in step 3. 
    if bank_account:
        try:
            bank_account.deposit("abc")
        except Exception as e:
            print("Error depositing non-numeric value:", e)


    # 7. Attempt to deposit a negative value into the BankAccount create in step 3. 
    if bank_account:
        try:
            bank_account.deposit(-50)
        except Exception as e:
            print("Error depositing negative value:", e)


    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount create in step 3. 
    if bank_account:
        try:
            bank_account.withdraw(100)
        except Exception as e:
            print("Error withdrawing valid amount:", e)


    # 9. Attempt to withdraw a non-numeric value from the BankAccount create in step 3. 
    if bank_account:
        try:
            bank_account.withdraw("xyz")
        except Exception as e:
            print("Error withdrawing non-numeric value:", e)


    # 10. Attempt to withdraw a negative value from the BankAccount create in step 3. 
    if bank_account:
        try:
            bank_account.withdraw(-50)
        except Exception as e:
            print("Error withdrawing negative value:", e)


    # 11. Attempt to withdraw a value from the BankAccount create in step 3 which 
    # exceeds the current balance of the account. 
    if bank_account:
        try:
            bank_account.withdraw(600)
        except Exception as e:
            print("Error withdrawing amount exceeding balance:", e)
 

    # 12. Code a statement which prints the BankAccount instance created in step 3. 
    if bank_account:
        try:
            print(bank_account)
        except Exception as e:
            print("Error printing BankAccount instance:", e)
  


if __name__ == "__main__":
    main()