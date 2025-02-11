class Person:
    def __init__(self, lastname, firstname, weight, height, address): # Konstruktor
        self.lastname = lastname
        self.firstname = firstname
        self.weight = weight
        self.height = height
        self.address = address

    def say_hello(self):
        return f'Hallo, ich bin {self.firstname} {self.lastname}'
    def __repr__(self):
        return f"Ich bin eine Person"

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
    def __repr__(self):
        return f'Address: city={self.city}, street={self.street}'
    def __eq__(self, other):
        if isinstance(other, Address):
           return (self.city.lower() == other.city.lower()) and (self.street.lower() == other.street.lower())
        else:
            return False 

def main():
    address_in_munich = Address('München', 'Marienplatz')
    address_in_berlin = Address('Berlin', 'Alexanderplatz')
    address_in_munich2 = Address('München', 'MARIENPLATZ')
    person1 = Person('Sawitzki', 'Rainer', 75.3, 183, address_in_munich)
    person2 = Person('Musterfrau', 'Andrea', 55.3, 158, address_in_berlin)
    person3 = Person('Musterfrau', 'Andrea', 55.3, 158, address_in_berlin)

    print(address_in_munich2 == address_in_munich)

if __name__ == '__main__':
    main()
