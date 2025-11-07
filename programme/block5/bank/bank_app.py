from bank import BankAccount
def main():
    account = BankAccount('Sawitzki')
    account.deposit(100)
    print(account.get_balance())
    account.withdraw(75)
    print(account.get_balance())

main()