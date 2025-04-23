class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Person(name={self.name})"
class Address:
    def __init__(self, address):
        self.address = address
    def __repr__(self):
        return f"Address(address={self.address})"
    def __eq__(self, other):
        if isinstance(other, Address):
            return self.address == other.address
        else:
            return False
    def __hash__(self):
        return hash(self.address)

p1 = Person('Sawitzki')
p2 = Person('Musterperson')
p3 = Person('Sawitzki')

people = {p1, p2, p3, p1}
print(len(people))
print(hash(p1))

a1 = Address('München')
a2 = Address('Berlin')
a3 = Address('München')

print(hash(a1))

addresses = {a1, a2, a3, a1}
print(len(addresses))



