""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, new_balance):
        if isinstance(new_balance, (int, float)) and new_balance >= 0:
            self.balance = new_balance
        else:
            print("Invalid balance amount. Please enter a positive number.")




    # The method sets the interest gained for the account.
    def set_interest(self, new_interest):
        if isinstance(new_interest, (int, float)) and new_interest >= 0:
            self.interest = new_interest
        else:
            print("Invalid interest amount.")

