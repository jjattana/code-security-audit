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
