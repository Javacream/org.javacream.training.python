class Person(object):
    def __init__(self, lastname, firstname, address):
        self.lastname = lastname
        self.firstname = firstname
        self.address = address
    def say_hello(self):
        greeting = f'Hallo, mein Name ist {self.firstname} {self.lastname}'
        return greeting
    def __repr__(self):
        return f'Person: lastname={self.lastname}, firstname={self.firstname}, address={self.address}'

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
    def __repr__(self):
        return f'Address: city={self.city}, street={self.street}'
    def __eq__(self, other):
        return (self.city == other.city) and (self.street == other.street)
    def __hash__(self):
        return hash(self.city) + hash(self.street)


def main():
    address_in_munich = Address("München", "Marienplatz")
    address_in_berlin = Address("Berlin", "Alexanderplatz")
    address_in_munich2 = Address("München", "Karlsplatz")
    address_in_munich3 = Address("München", "Karlsplatz")
    address_in_munich4 = address_in_munich3

    person1 = Person("Sawitzki", "Rainer", address_in_munich) 
    person2 = Person("Musterfrau", "Hannah", address_in_berlin)
    print(address_in_munich == address_in_berlin)
    print(address_in_munich == address_in_munich2)
    print(address_in_munich3 == address_in_munich2)
    print(address_in_munich3 == address_in_munich4)

    address_set = {address_in_munich, address_in_berlin, address_in_munich2, address_in_munich3, address_in_munich4}
    print(len(address_set))

    print('done')

if __name__ == '__main__':
    main()
