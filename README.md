# Customer Banking System

## Overview

This project is part of the Module 3 Challenge for Columbia University's AI Bootcamp. The goal is to create a customer banking system that allows users to calculate and track interest earned on savings and CD accounts. Users can input their savings and CD account details, see the interest earned, and view the updated balances after a specified number of months.

## Project Structure

The project consists of the following Python files:

- `Account.py`: Contains the `Account` class with methods to set the balance and interest.
- `savings_account.py`: Implements the `create_savings_account` function to create a savings account instance, calculate interest based on user input, update the account balance with earned interest, and return the updated balance and interest earned.
- `cd_account.py`: Similar to `savings_account.py`, but for creating and managing CD accounts.
- `customer_banking.py`: The main program file. It imports functions from `savings_account.py` and `cd_account.py` and includes a `main` function that prompts the user for account details, calls the corresponding functions to calculate interest, updates balances, and displays results.

## Usage

To use the system, run `customer_banking.py`. The program will guide you through entering your savings and CD account details and then display the calculated interest and updated account balances.

## Development Notes

- Ensure to follow the interest calculation formulas as per the challenge requirements.
- Inputs are validated for type and value correctness.
- Code is modular and follows Python best practices for readability and maintainability.

## Acknowledgements

This project was completed as part of the curriculum at Columbia University's AI Bootcamp. All code was authored by [Your Name], with guidance and instructions provided by the course materials.

## Contact

For any queries or feedback regarding this project, please reach out to KenStager@hotmail.com

