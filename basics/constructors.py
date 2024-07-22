class Person:
    def __init__ (self, lastname, firstname, address):
        if lastname == None:
            raise Exception("unable to create person, lastname is mandatory")
        if firstname == None:
            raise Exception("unable to create person, firstname is mandatory")
        if address == None:
            raise Exception("unable to create person, firstname is mandatory")
        self.lastname = lastname
        self.firstname = firstname
        self.address = address
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
        
def main():
    a1 = Address("Marienplatz", "München")
    p1 = Person("Sawitzki", "Rainer", a1)
    print(p1.greet())
main()
