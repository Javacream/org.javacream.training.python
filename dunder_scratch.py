from  people import Person, Address

def identity():
    p1 = Person('A', 'B')
    p2 = Person('C', 'D')
    p3 = Person('A', 'B')

    print(p1 == p2)
    print(p1 == p3)

    a1 = Address('A', 'B')
    a2 = Address('C', 'D')
    a3 = Address('A', 'B')

    print(a1 == a2)
    print(a1 == a3)

    s1 = str('A')
    s2 = str('C')
    s3 = str('A')

    print(s1 == s2)
    print(s1 == s3)

    print(s1.__eq__(s2))
    print(s1.__eq__(s3))

def print_out():
    a1 = Address('A', 'B')
    print(a1)
    print(repr(a1))
    print(a1.__repr__())

def duplicates():
    p1 = Person('A', 'B')
    p2 = Person('C', 'D')
    p3 = Person('A', 'B')
    people_set = {p1, p2, p3, p1, p3}
    print(len(people_set))

    a1 = Address('A', 'B')
    a2 = Address('C', 'D')
    a3 = Address('A', 'B')
    address_set = {a1, a2, a3, a1, a3}
    print(len(address_set))

class Money:
    def __init__(self, amount):
        self.amount = amount
    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount
        else:
            return False
    def __hash__(self):
        return hash(self.amount)
    def __repr__(self):
        return f'Money(amount={self.amount})'
    def __add__(self, other):
        return Money(self.amount + other.amount)
    def __add__(self, other):
        return Money(self.amount + other.amount)
    def __sub__(self, other):
        return Money(self.amount - other.amount)
    def __rmul__(self, other):
        return Money(self.amount * other)
    def __truediv__(self, other):
        return Money(self.amount / other)


def money():
    m1 = Money(20)
    m2 = Money(22)
    m3 = m1 + m2
    print(m3)
    print(5*m1)
    print(m1/5)

def main():
    #identity()
    #print_out()
    # duplicates()
    money()
if __name__ == '__main__':
    main()