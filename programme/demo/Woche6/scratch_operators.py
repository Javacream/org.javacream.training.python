class Money:
    def __init__(self, amount):
        self.amount = amount
    def __repr__(self):
        return f'Money: amount={self.amount}'
    def __eq__(self, other):
        return self.amount == other.amount
    def __lt__(self, other):
        return self.amount < other.amount
    def __add__(self, other):
        return Money(self.amount + other.amount)

def main():
    money1 = Money(10)
    money2 = Money(5)
    money3 = Money(10)
    print(money1 == money2)
    print(money1 == money3)

    print(money1 + money3)

if __name__ == '__main__':
    main()

