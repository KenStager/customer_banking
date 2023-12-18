# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account


def get_float_input(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value >= 0:
                    return value
                else:
                    print("Invalid input. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")


def get_int_input(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value >= 0:
                    return value
                else:
                    print("Invalid input. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = get_float_input("Enter initial savings balance: $")
    savings_interest = get_float_input("Enter savings interest rate (%): ")
    savings_maturity = get_int_input("Enter the duration in months: ")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Updated savings balance: ${updated_savings_balance:,.2f}")
    print(f"Interest earned on savings: ${interest_earned:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = get_float_input("\nEnter initial CD balance: $")
    cd_rate = get_float_input("Enter CD interest rate (%): ")
    cd_months = get_int_input("Enter the duration in months: ")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_rate, cd_months)
    print(f"Updated CD balance: ${updated_cd_balance:,.2f}")
    print(f"Earned interest on the CD: ${interest_earned:,.2f}")

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

if __name__ == "__main__":
    # Call the main function.
    main()