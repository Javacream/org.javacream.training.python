class Money:
    def __init__(self, amount):
        self.amount = amount
    def __repr__(self):
        return f'Money(amount={self.amount})'
    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount
        else:
            return False
    def __hash__(self):
        return hash(self.amount)
    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        else:
            raise Exception('+ not supported')


m1 = Money(20)
m2 = Money(22)
print(m1, m2)
print(m1 == m2)
m3 = m1 + m2
print(m3)