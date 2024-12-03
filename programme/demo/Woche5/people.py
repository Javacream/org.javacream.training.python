class Person:
    def __init__(self, lastname, firstname, weight, address):
        self.lastname = lastname 
        self.firstname = firstname
        self.weight = weight
        self.address = address
        address.people.append(self)
    def say_hello(self):
        message = f"Hallo, mein Name ist {self.firstname} {self.lastname}"
        return message
    
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
        self.people = list()
    def get_address(self):
        return f'Addresse: {self.street}, {self.city}'