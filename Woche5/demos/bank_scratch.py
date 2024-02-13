class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):    
        self.balance += money
    def pay_off(self, money):
        self.balance -= money
    def get_balance(self):
        return self.balance

def main():

    account1 = BankAccount("Sawitzki", 100)
    account1.deposit(10)
    print(account1.get_balance())
main()