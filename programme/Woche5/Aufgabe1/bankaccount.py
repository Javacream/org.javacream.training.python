class BankAccount:
    def __init__(self, customer):
        self.__customer = customer
        self.__account = 0
    def get_account(self):
        return f'Das Konto für {self.__customer} hat einen Kontostand von {self.__account}'
    
    def deposit(self, amount):
        if amount <= 0:
            error = Exception(f'amount must be positive, not {amount}')
            raise error
        self.__account += amount    

    def payout(self, amount):
        if amount <= 0:
            raise Exception(f'amount must be positive, not {amount}')
        self.__account -= amount                