from collections.abc import Iterable


class Person:
    def __init__ (self, lastname, firstname, address):
        if lastname == None:
            raise Exception("unable to create person, lastname is mandatory")
        if firstname == None:
            raise Exception("unable to create person, firstname is mandatory")
        if address == None:
            raise Exception("unable to create person, address is mandatory")
        self.lastname = lastname
        self.firstname = firstname
        self.address = address
    def __repr__(self):
        return f'Person: lastname={self.lastname}, firstname={self.firstname}'    
    
    def greet(self):
        greeting =  f'Hello, i am {self.firstname} {self.lastname}, i live in {self.address.city}'
        return greeting    

class Address:
    def __init__(self, street, city):
        if street == None:
            raise Exception("unable to create address, street is mandatory")
        if city == None:
            raise Exception("unable to create address, city is mandatory")
        self.city = city
        self.street = street
    def __repr__(self):
        return f'Address: city={self.city}, street={self.street}'
    def __eq__(self, value):
        if value == None:
            return False
        return self.street == value.street
        
def main():
    a1 = Address("Marienplatz", "München")
    a2 = Address("Marienplatz", "München")
    p1 = Person("Sawitzki", "Rainer", a1)
    p2 = Person("Sawitzki", "Rainer", a1)
    s1 = str("Hugo")
    s2 = str("Hugo")

    #print(p1)
    print(dir(p1))
    print(a1 == a2)
    print(p1 == p2)
    print(s1 == s2)

main()
