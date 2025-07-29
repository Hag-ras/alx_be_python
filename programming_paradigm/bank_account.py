class BankAccount:
    def __init__(self, balance=0):
        self.account_balance = balance
    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: {amount}"
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return f"Withdrew: {amount}"
        else:
            return "Insufficient funds."

    def display_balance(self):
        return f"Current Balance: {self.account_balance}"
        