"""
Description: Defines the Client class with validation for client attributes and a formatted string representation.
Author: Jashanpreet Kaur Jattana
"""


from email_validator import EmailNotValidError, validate_email

class Client:
    def __init__(self, client_number, first_name, last_name, email_address):
        # Validate client_number
        if type(client_number) != int:  
            raise ValueError("Client number must be an integer.")
        self._client_number = client_number
        
        # Validate first_name
        first_name = first_name.strip()
        if not first_name:
            raise ValueError("First name cannot be blank.")
        self._first_name = first_name

        # Validate last_name
        last_name = last_name.strip()
        if not last_name:
            raise ValueError("Last name cannot be blank.")
        self._last_name = last_name
        
        # Validate email_address
        try:
            valid = validate_email(email_address)
            self._email_address = valid.email
        except EmailNotValidError:
            self._email_address = email_address
    
    # Property for client_number
    @property
    def client_number(self):
        """
        Returns the clients's ID
        :return: client number
        """
        return self._client_number
    
    # Property for first_name
    @property
    def first_name(self):
        """
        Returns the client's first name
        :returns: client's first name
        """
        return self._first_name
    
    # Property for last_name
    @property
    def last_name(self):
        """
        Returns the client's last name
        :returns: client's last name
        """
        return self._last_name
    
    # Property for email_address
    @property
    def email_address(self):
        """
        Returns the client's email address
        :returns: client's email address
        """
        return self._email_address
    
    # __str__ method
    def __str__(self):
        """
        Returns string representaion of client data
        :return: A string with the format "last_name, first_name [client_number] - email_address"
        """
        return f"{self._last_name}, {self._first_name} [{self._client_number}] - {self._email_address}"

