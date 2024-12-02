from bankaccount import BankAccount

def main():
    account = BankAccount('Musterperson')
    try:
        account.deposit(9.99)
        account.deposit(-12.22)
        account.payout(5)
    except Exception as e:
        print(f'error: {e}')
    print(account.get_account())

if __name__ == '__main__':
    main()