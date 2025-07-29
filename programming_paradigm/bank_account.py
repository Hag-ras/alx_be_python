class BankAccount:
    def __init__(self, balance=0):
        self.account_balance = balance
    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: {amount}"
    def withdraw(self, amount):
        result = self.account_balance - amount
        if result >= 0 :
            self.account_balance = result
            return f"Withdrew: {amount}"
        else:
            return "Insufficient funds."
    def display_balance(self):
        return f"Current Balance: {self.account_balance}"
        