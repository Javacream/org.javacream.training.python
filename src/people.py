class Person:
    # constructor
    def __init__(self, lastname, firstname, height, address):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.address = address
    def say_hello(self):
        return f'Hello, my name is {self.firstname} {self.lastname}, i live in {self.address.city}'

class Address:
    def __init__(self, city, postal_code, street):
        self.city = city; 
        self.street = street;
        self.postal_code = postal_code

def main():
    address = Address('München', 81371, 'Marienplatz')
    person1 = Person('Sawitzki', 'Rainer', 183, address)
    person2 = Person('Musterfrau', 'Hannah', 177, address)

    print(person1.say_hello(), person2.say_hello())
    print(type(person1), type(person2))

main()