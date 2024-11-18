from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()

        if isinstance(account, BankAccount):
            self.account = copy.deepcopy(account)
            
            self.account_number_label.setText(str(self.account.account_number))
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            self.deposit_button.clicked.connect(self.on_apply_transaction)
            self.withdraw_button.clicked.connect(self.on_apply_transaction)
            self.exit_button.clicked.connect(self.on_exit)
        
        else:
            QMessageBox.warning(self, "Invalid Account", "The provided account is not valid.")
            self.reject()

    def on_apply_transaction(self) -> None:

        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Deposit Failed", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return

        try:
            sender = self.sender()
            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)
            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)
            else:
                return 

            self.balance_label.setText(f"${self.account.balance:,.2f}")

            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Transaction Failed",
                f"{transaction_type} Failed: {str(e)}"
            )
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    def on_exit(self) -> None:
        """
        Closes the Account Details window and returns the user to the Client Lookup Window.
        """
        self.close()