"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: Jashanpreet Kaur Jattana
Date: 2024-09-14
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client
from email_validator import EmailNotValidError, validate_email

class TestClient(unittest.TestCase):
    
    def test_init_valid(self):
        """
        Verifies that the client class works properly when given correct information and that all the details are set correctly"
        """
        client = Client(101, "Jashanpreet", "Jattana", "jjattana@pixell-river.com")
        self.assertEqual(client.client_number, 101)
        self.assertEqual(client.first_name, "Jashanpreet")
        self.assertEqual(client.last_name, "Jattana")
        self.assertEqual(client.email_address, "jjattana@pixell-river.com")

    
    def test_init_invalid_client_number(self):
        """
        Ensures that if the client_number is not an integer, ValueError is raised
        """
        with self.assertRaises(ValueError):
            Client("abc", "Jashanpreet", "Jattana", "jjattana@pixell-river.com")
    
    
    def test_init_blank_first_name(self):
        """
        Ensures that if the first_name is blank, ValueError is raised
        """
        with self.assertRaises(ValueError):
            Client(101, "  ", "Jattana", "jjattana@pixell-river.com")

    
    def test_init_blank_last_name(self):
        """
        Ensures that if the last_name is blank, ValueError is raised
        """
        with self.assertRaises(ValueError):
            Client(101, "Jashanpreet", "  ", "jjattana@pixell-river.com")

   
    def test_init_invalid_email_address(self):
        """
        If the email address is invlaid, raises EmailNotValidError
        """
        with self.assertRaises(EmailNotValidError):
            Client(101, "Jashanpreet", "Jattana", "invalid-email")

    
    def test_client_number(self):
        """
        Ensures that client_number property returns correct value
        """
        client = Client(101, "Jashanpreet", "Jattana", "jjattana@pixell-river.com")
        self.assertEqual(client.client_number, 101)

    
    def test_first_name(self):
        """
        Ensures that first_name property returns correct value
        """
        client = Client(101, "Jashanpreet", "Jattana", "jjattana@pixell-river.com")
        self.assertEqual(client.first_name, "Jashanpreet")

    
    def test_last_name(self):
        """
        Ensures last_name property returns correct value
        """
        client = Client(101, "Jashanpreet", "Jattana", "jjattana@pixell-river.com")
        self.assertEqual(client.last_name, "Jattana")

    
    def test_email_address(self):
        """
        Ensures email_address property returns correct value
        """
        client = Client(101, "Jashanpreet", "Jattana", "jjattana@pixell-river.com")
        self.assertEqual(client.email_address, "jjattana@pixell-river.com")

    
    def test_str(self):
        """
        Ensures __str__ method returns correct string representaion of client data 
        """
        client = Client(101, "Jashanpreet", "Jattana", "jjattana@pixell-river.com")
        self.assertEqual(str(client), "Jattana, Jashanpreet [101] - jjattana@pixell-river.com")

if __name__ == '__main__':
    unittest.main()