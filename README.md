# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each 
assignment will build on the work done in the previous assignment(s).  Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
Jashanpreet Kaur Jattana

## Assignment
Assignment 1: Classes, Encapsulation and Unit Test Planning. This assignment involves creating basic classes that will be part of a larger system. These classes will focus on using concepts from Module 01, especially encapsulation. This means that important information will be kept private within the class, and only accessed or changed using specific public methods called accessors and setters mutators.

## Encapsulation
Encapsulation in the `BankAccount` and `Transaction` classes is done by restricting direct access to the class attributes and providing controlled access through public methods. Private attributes, like `account_number`, `client_number`, and `balance`, are protected using name mangling (with double underscores, such as `__account_number`), which stops them from being accessed or changed directly from outside the class.

## Assignment 2
In this assignment, I will extend the `BankAccount` class by creating new types of accounts as subclasses. These new account types will inherit common features from `BankAccount`, but each one will have its own special version of a method. This demonstrates polymorphism, where different objects can use the same method in their own unique way. The focus is to show how this works and to test that each subclass behaves as expected.

## Polymorphism

Polymorphism in this assignment was achieved through method overriding in the `BankAccount` subclasses: `ChequingAccount`, `SavingsAccount`, and `InvestmentAccount`. Each subclass implements its own version of the `get_service_charges()` and `__str__()` methods, allowing them to provide specific behaviors while maintaining a common interface defined in the `BankAccount` class. This enables different account types to be used interchangeably, allowing for dynamic behavior based on the object's actual class.

## Assignment 3
 In this assignment the Strategy Pattern will be applied to simplify and add scalability to the service charge functionality. In addition, the Observer Pattern will be introduced. Using the Observer Pattern a client will be notified whenever a large transaction takes place and/or whenever an account balance drops below a minimum value.

## Strategy Pattern

The Strategy Pattern is implemented in this application to manage different methods for calculating service charges for bank accounts, such as Chequing, Savings, and Investment accounts. A common interface defines the calculation method that each account type follows, allowing for customized calculations. Each account type has its own approach: ChequingAccount calculates charges based on overdraft limits and transactions, SavingsAccount focuses on maintaining a minimum balance, and InvestmentAccount bases charges on the investment duration. The main program (A02_main.py) demonstrates this pattern by creating account instances and invoking `get_service_charges()`, applying the relevant strategy for each. This design offers flexibility in adding new account types, separates strategy logic from account classes for improved readability, and encapsulates charge logic within each account class, exposing only necessary methods.

## Observer Pattern
The Observer Pattern in this application allows clients to receive automatic notifications about important account activities, such as large transactions or low balances. It establishes a one-to-many relationship where account objects (called Subjects) inform client objects (called Observers) about updates without the clients needing to check for changes constantly. Account classes like ChequingAccount and SavingsAccount act as Subjects, maintaining a list of clients that they notify when certain events, like high-value transactions, occur. The Client class serves as the Observer, receiving alerts for specific changes in the account. When a significant transaction happens, the account sends notifications to each subscribed client with relevant details, keeping them informed in real-time. The main program shows this pattern by linking Client objects to accounts, enabling notifications based on specific events. The benefits include immediate updates for clients, less dependency between clients and accounts, and the ability to easily add more clients or account types without significant code changes.

## Assignment 4
In this assignment, I will create a responsive Windows application using PySide6, focusing on event handling, inheritance, and data management. The application will interact dynamically with the user by responding to events such as clicks and key presses, using signals and slots. I will extend provided superclasses to customize the window design, demonstrating the power of inheritance in object-oriented programming. The application will manage data through Python dictionaries, reading from files (e.g., JSON or CSV), and dynamically processing and displaying this data in the UI. The goal is to build a flexible, responsive app that adapts to different screen sizes while allowing users to interact with and manipulate data in real-time. This project will enhance MY skills in event-driven programming, OOP, and data management with PySide6.