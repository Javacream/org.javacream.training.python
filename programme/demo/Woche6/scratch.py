class Money:
    def __init__(self, amount):
        self.amount = amount
    def __repr__(self):
        return f'Money: amount={self.amount}'
    def __eq__(self, other):
        return self.amount == other.amount
    def __hash__(self):
        return hash(self.amount)
    def __lt__(self, other):
        return self.amount < other.amount
    def __add__(self, other):
        return Money(self.amount + other.amount)
def main():
    m1 = Money(20)
    m2 = Money(5)

    print (m1 > m2)
    m3 = m1 + m2
    print(m3)
if __name__ == '__main__':
    main()