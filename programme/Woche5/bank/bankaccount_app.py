from bankaccount import BankAccount

def main():
    account = BankAccount('Musterperson')
    account.deposit(9.99)
    print(account.get_account())
    account.deposit(12.22)
    account.payout(5)
    print(account.get_account())

if __name__ == '__main__':
    main()