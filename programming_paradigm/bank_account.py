#Class Definition
class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance 

    def deposit(self,amount):
        self._account_balance += amount
        return self._account_balance
    
    def withdraw(self,amount):
        if amount > self._account_balance:
           return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")
