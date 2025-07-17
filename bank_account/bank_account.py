class BankAccount:
    def __init__(self, bal=0):
        
        """Initialize account with optional balance (default is 0)."""

        self.bal = bal


    def deposit(self, deposit_money):

        """Deposit money into the account."""

        if deposit_money <= 0:

            print("Deposit amount must be greater than zero.")

            return
        
        self.bal += deposit_money

        print(f"You have deposited ₹{deposit_money}.")

        self.display_balance()


    def withdrawal(self, withdrawal_money):

        """Withdraw money from the account."""

        if withdrawal_money > self.bal:

            print("Sorry, insufficient balance.")

        elif withdrawal_money <= 0:

            print("Please enter a valid amount greater than zero.")

        else:

            self.bal -= withdrawal_money

            print(f"You have withdrawn ₹{withdrawal_money}.")

            self.display_balance()

    def display_balance(self):

        """Display the current account balance."""

        print(f"Current balance: ₹{self.bal}")
