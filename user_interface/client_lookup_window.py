from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    def __init__(self):
        """
        Initializes the ClientLookupWindow with data and sets up event connections.
        """
        # Step 1: Call the superclass initializer
        super().__init__()

        # Step 2: Load client and account data
        self.client_listing, self.accounts = load_data()

        # Step 3: Connect the lookupButton to on_lookup_client()
        self.lookupButton.clicked.connect(self.on_lookup_client)

        # Step 4: Connect the accountTable to on_select_account()
        self.accountTable.cellClicked.connect(self.on_select_account)

    def on_lookup_client(self):
        """Handles the lookup process for a client based on the entered client number."""
        # Step 1: Retrieve and validate client number
        client_number_text = self.client_number_edit.text().strip()
        
        try:
            client_number = int(client_number_text)
        except ValueError:
            # If input is non-numeric, show an error message
            QMessageBox.information(self, "Input Error", "The client number must be a numeric value.")
            self.reset_display()
            return

        # Step 2: Check if client exists
        if client_number not in self.client_listing:
            QMessageBox.information(self, "Not Found", f"Client number: {client_number} not found.")
            self.reset_display()
            return

        # Step 3: Client found, update display
        client = self.client_listing[client_number]
        self.client_info_label.setText(f"Client Name: {client.get_full_name()}")

        # Clear existing rows in the account table
        self.accountTable.setRowCount(0)

        # Step 4: Populate account table
        for account in self.accounts.values():
            if account.client_number == client_number:
                row_position = self.accountTable.rowCount()
                self.accountTable.insertRow(row_position)

                # Add data to the table row
                account_number_item = QTableWidgetItem(str(account.account_number))
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                date_created_item = QTableWidgetItem(str(account.date_created))
                account_type_item = QTableWidgetItem(account.__class__.__name__)

                # Align text in cells to center
                account_number_item.setTextAlignment(Qt.AlignCenter)
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                date_created_item.setTextAlignment(Qt.AlignCenter)
                account_type_item.setTextAlignment(Qt.AlignCenter)

                # Add items to the table
                self.accountTable.setItem(row_position, 0, account_number_item)
                self.accountTable.setItem(row_position, 1, balance_item)
                self.accountTable.setItem(row_position, 2, date_created_item)
                self.accountTable.setItem(row_position, 3, account_type_item)

        # Resize columns to fit content
        self.accountTable.resizeColumnsToContents()
    
    @Slot(int, int)
    def on_select_account(self, row: int, column: int) -> None:
        """Handles the selection of an account from the table to open the Account Details window."""
        # Step 1: Retrieve the account number from the selected row
        account_number_item = self.accountTable.item(row, 0)  # Column 0 holds the account number
        account_number = account_number_item.text() if account_number_item else ""

        # Step 2: Check if the account_number is blank
        if not account_number:
            QMessageBox.information(self, "Invalid Selection", "The selected account is invalid.")
            return

        # Step 3: Check if the account exists in the accounts dictionary
        if int(account_number) not in self.accounts:
            QMessageBox.information(self, "Bank Account does not Exist", "The selected bank account does not exist.")
            return

        # Step 4: Obtain the BankAccount object
        bank_account = self.accounts[int(account_number)]

        # Step 5: Open the Account Details window
        account_details_window = AccountDetailsWindow(bank_account)
        account_details_window.exec_()
       
