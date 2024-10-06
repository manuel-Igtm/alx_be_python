
class BankAccount:
    def __init__(self, account_balance = 0.0):
        #Initialize the account with an optional initial balance.
        self.account_balance = account_balance  # Encapsulated attribute

    def deposit(self, amount):
        #Deposit a specified amount to the account balance.
        # if amount > 0:
            self.account_balance = self.account_balance + amount
        # else:
        #     print("Deposit amount must be positive.")

    def withdraw(self, amount):
        #Withdraw a specified amount from the account balance if sufficient funds are available.
        if 0 < amount <= self.account_balance:
            self.account_balance = self.account_balance - amount
            return True
        else:
            return False

    def display_balance(self):
        #Print the current account balance.
        print(f"Current Balance: ${self.account_balance:.2f}")


