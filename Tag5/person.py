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
        return f"Person"

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
    def __hash__(self):
        return hash(self.city.lower()) + hash(self.street.lower())

def main():
    address_in_munich = Address('München', 'Marienplatz')
    address_in_berlin = Address('Berlin', 'Alexanderplatz')
    address_in_munich2 = Address('München', 'MARIENPLATZ')
    person1 = Person('Sawitzki', 'Rainer', 75.3, 183, address_in_munich)
    person2 = Person('Musterfrau', 'Andrea', 55.3, 158, address_in_berlin)
    person3 = Person('Musterfrau', 'Andrea', 55.3, 158, address_in_berlin)

    people_set = {person1, person2, person3}
    print(len(people_set))

    address_set = {address_in_munich, address_in_berlin, address_in_munich2}
    print(len(address_set))
if __name__ == '__main__':
    main()
