class BankAccount:
    def __init__(self, customer):
        self.customer = customer
        self.account = 0
    def get_account(self):
        return self.account
    
    def deposit(self, amount):
        if amount <= 0:
            print(f'amount must be positive, not {amount}')
        else:
            self.account += amount    

    def payout(self, amount):
        if amount <= 0:
            print(f'amount must be positive, not {amount}')
        else:
            self.account -= amount                