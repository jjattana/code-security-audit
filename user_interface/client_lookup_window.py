from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    A window for looking up and managing client and account details.

    Inherits:
        LookupWindow: Base class for lookup windows.

    Attributes:
        client_listing (dict): A dictionary mapping client numbers to Client objects.
        accounts (dict): A dictionary mapping account numbers to BankAccount objects.

    Methods:
        __init__():
            Initializes the ClientLookupWindow, loads data, and sets up event connections.
        on_lookup_client():
            Handles client lookups by client number, displaying relevant client and account data.
        on_select_account(row, column):
            Opens the AccountDetailsWindow for the selected account from the table.
        update_data(account):
            Updates the account balance in the account table and persists the change.
        __on_select_account(row, column):
            Handles account selection and ensures valid account details are displayed.
    """
    def __init__(self):
        """
        Initializes the ClientLookupWindow with data and sets up event connections.
        """
        super().__init__()

        self.client_listing, self.accounts = load_data()

        self.lookup_button.clicked.connect(self.on_lookup_client)

        self.account_table.cellClicked.connect(self.on_select_account)

        self.filter_button.clicked.connect(self.on_filter_clicked)

    def on_lookup_client(self):
        """Handles the lookup process for a client based on the entered client number."""
        client_number_text = self.client_number_edit.text().strip()
        
        try:
            client_number = int(client_number_text)
        except ValueError:
            QMessageBox.information(self, "Input Error", "The client number must be a numeric value.")
            self.reset_display()
            return

        if client_number not in self.client_listing:
            QMessageBox.information(self, "Not Found", f"Client number: {client_number} not found.")
            self.reset_display()
            return

        client = self.client_listing[client_number]
        self.client_info_label.setText(f"Client Name: {client.get_full_name()}")

        self.account_table.setRowCount(0)

        for account in self.accounts.values():
            if account.client_number == client_number:
                row_position = self.account_table.rowCount()
                self.account_table.insertRow(row_position)

                account_number_item = QTableWidgetItem(str(account.account_number))
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                date_created_item = QTableWidgetItem(str(account.date_created))
                account_type_item = QTableWidgetItem(account.__class__.__name__)

                account_number_item.setTextAlignment(Qt.AlignCenter)
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                date_created_item.setTextAlignment(Qt.AlignCenter)
                account_type_item.setTextAlignment(Qt.AlignCenter)

                self.account_table.setItem(row_position, 0, account_number_item)
                self.account_table.setItem(row_position, 1, balance_item)
                self.account_table.setItem(row_position, 2, date_created_item)
                self.account_table.setItem(row_position, 3, account_type_item)

        self.account_table.resizeColumnsToContents()
        self.toggle_filter(False)
    
    @Slot(int, int)
    def on_select_account(self, row: int, column: int) -> None:
        """Handles the selection of an account from the table to open the Account Details window."""
        account_number_item = self.account_table.item(row, 0)
        account_number = account_number_item.text() if account_number_item else ""

        if not account_number:
            QMessageBox.information(self, "Invalid Selection", "The selected account is invalid.")
            return

        if int(account_number) not in self.accounts:
            QMessageBox.information(self, "Bank Account does not Exist", "The selected bank account does not exist.")
            return

        bank_account = self.accounts[int(account_number)]

        account_details_window = AccountDetailsWindow(bank_account)
        account_details_window.exec_()

    def update_data(self, account: BankAccount) -> None:
        """
        Updates the account balance in the account_table and accounts dictionary.
        """

        for row in range(self.account_table.rowCount()):
            account_number_in_table = self.account_table.item(row, 0).text()

            if account_number_in_table == str(account.account_number):

                self.account_table.setItem(row, 1, 
                                           QTableWidgetItem(f"${account.balance:,.2f}"))

                self.accounts[account.account_number] = account

                update_data(account)
                break

    def on_filter_clicked(self):
        """
        Handles the filtering of account records based on user-defined criteria.
        """
        if self.filter_button.text() == "Apply Filter":
            # Get the selected column index and the filter text
            filter_column = self.filter_combo_box.currentIndex()
            filter_text = self.filter_edit.text().strip().lower()

            for row in range(self.account_table.rowCount()):
                # Get the cell text for the specified column in the current row
                cell_item = self.account_table.item(row, filter_column)
                cell_text = cell_item.text().strip().lower() if cell_item else ""

                # Determine whether to hide the row based on the filter text
                if filter_text not in cell_text:
                    self.account_table.setRowHidden(row, True)
                else:
                    self.account_table.setRowHidden(row, False)

            self.toggle_filter(filter_applied=True)
        else:
            # Reset the filtering to show all rows
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.toggle_filter(filter_applied=False)

    def toggle_filter(self, filter_on: bool) -> None:
        """
        Toggles the display of the filter widgets to indicate whether filtering is currently in place.

        Args:
        filter_on (bool): True if filtering is applied, False otherwise.
        """
        self.filter_button.setEnabled(True)

        if filter_on:
            # Filtering is ON
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            # Filtering is OFF
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.clear()  # Clear the filter_edit text
            self.filter_combo_box.setCurrentIndex(0)  # Reset combobox to the first option

            # Show all rows in the account table
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered")

       
