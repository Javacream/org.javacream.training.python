class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.balance = balance
        self.owner = owner
    def deposit(self, amount: float):
        if amount <= 0:
            e = Exception(f'cannot deposit a negative amount {amount}')
            raise e
        self.balance = self.balance + amount
    def withdraw(self, amount: float):
        if amount <= 0:
            raise Exception(f'cannot withdraw a negative amount {amount}')
        self.balance = self.balance - amount
        
    def get_balance(self) ->  float:
        return self.balance
