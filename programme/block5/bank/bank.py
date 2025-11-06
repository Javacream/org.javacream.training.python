class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount:float):
        if amount >= 0:
            self.balance = self.balance + amount
    def withdraw(self, amount: float):
        if amount >= 0:
            self.balance -= amount
        else:
            raise Exception(f'you cannot withdraw a negative amount: {amount} ')

    def get_balance(self):
        return self.balance