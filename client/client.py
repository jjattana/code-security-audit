"""
Description: Defines the Client class with validation for client attributes and a formatted string representation.
Author: Jashanpreet Kaur Jattana
"""

from datetime import datetime
from email_validator import EmailNotValidError, validate_email
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email

class Client:
    """
    Description:
        The `Client` class represents a bank client with attributes for client number, name, and email address. 
        It includes validation for input attributes, provides properties for accessing these attributes, 
        and integrates with the Observer pattern to receive updates and simulate email notifications.

    Attributes:
        None 
    """
    def __init__(self, client_number, first_name, last_name, email_address):
        """
        Description:
            Initializes a `Client` object with validated attributes for client number, first name, 
            last name, and email address.

        Args:
            client_number (int): The unique identifier for the client.
            first_name (str): The client's first name. Cannot be blank.
            last_name (str): The client's last name. Cannot be blank.
            email_address (str): The client's email address. Validates format and assigns it.

        Raises:
            ValueError: If client number is not an integer, or if first/last name is blank.
            EmailNotValidError: If the provided email address is invalid.
        """
        # Validate client_number
        if type(client_number) != int:  
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number
        
        # Validate first_name
        first_name = first_name.strip()
        if not first_name:
            raise ValueError("First name cannot be blank.")
        self.__first_name = first_name

        # Validate last_name
        last_name = last_name.strip()
        if not last_name:
            raise ValueError("Last name cannot be blank.")
        self.__last_name = last_name
        
        # Validate email_address
        try:
            valid = validate_email(email_address)
            self.__email_address = valid.email
        except EmailNotValidError:
            self.__email_address = email_address
    
    # Property for client_number
    @property
    def client_number(self):
        """
        Retrieves the client's unique identifier.

        Args:
            None

        Returns:
            int: The client number.
        """
        return self.__client_number
    
    # Property for first_name
    @property
    def first_name(self):
        """
        Retrieves the client's first name.

        Args:
            None

        Returns:
            str: The first name of the client.
        """
        return self.__first_name
    
    # Property for last_name
    @property
    def last_name(self):
        """
        Retrieves the client's last name.

        Args:
            None

        Returns:
            str: The last name of the client.
        """
        return self.__last_name
    
    # Property for email_address
    @property
    def email_address(self):
        """
        Retrieves the client's email address.

        Args:
            None

        Returns:
            str: The email address of the client.
        """
        return self.__email_address
    
    # __str__ method
    def __str__(self):
        """
        Provides a string representation of the client's information.

        Args:
            None

        Returns:
            str: A string in the format "last_name, first_name [client_number] - email_address".
        """
        return f"{self.__first_name}, {self.__last_name} [{self.__client_number}] - {self.__email_address}"

    # Update method for Observer pattern
    def update(self, message: str) -> None:
        """
        Receives a notification and simulates sending an email with the alert details.
        
        Args:
            message (str): The message containing update information from the subject.

        Returns:
            None
        """
        subject = f"ALERT: Unusual Activity: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        email_message = f"Notification for {self.client_number}: {self.first_name} {self.last_name}: {message}"
        
        # Simulate sending the email
        simulate_send_email(self.email_address, subject, email_message)