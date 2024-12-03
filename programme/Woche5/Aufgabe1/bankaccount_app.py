from bankaccount import BankAccount

def main():
    account = BankAccount('Musterperson')
    try:
        account.deposit(9.99)
        account.deposit(12.22)
        account.payout(5)
        # account.__account = 666 -> ignoriert, privates Attribut
        account._BankAccount__account = 666 # geht, ein privates Attribut wird nur "komisch" umbenannt
    except Exception as e:
        print(f'error: {e}')
    print(account.get_account())

if __name__ == '__main__':
    main()