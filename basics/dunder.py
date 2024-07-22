class Money:
    def __init__(self, amount) -> None:
        self.amount = amount
    def __repr__(self) -> str:
        return f'Money with amount {self.amount}'
    def __eq__(self, value: object) -> bool:
        return self.amount == value.amount
    def __gt__(self, other):
        return self.amount > other.amount
    def __lt__(self, other):
        return self.amount < other.amount
    def __add__(self, other):
        return Money(self.amount + other.amount)


def main():
    m1 = Money(42)
    m2 = Money(42)
    m3 = Money(2)

    print(m1)
    print (m1 == m2)
    print (m1 > m3)
    print (m1 < m3)
    m4 = m1 + m3
    print(m4)
main()