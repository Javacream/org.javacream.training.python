class Money:
    def __init__(self, amount):
        self.amount = amount
    def __repr__(self):
        return f'Money: amount={self.amount}'
    def __add__(self, other):
        return Money(self.amount + other.amount)

def main():
    m1 = Money(2)
    m2 = Money(40)

    m3 = m1 + m2
    print(m3)

    l1 = ["a", "b"]
    l2 = ["c", "d", "e"]
    l3 = l1 + l2
    print(l3)
if __name__ == '__main__':
    main()
