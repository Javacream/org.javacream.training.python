class Person:
    def __init__(self, lastname, firstname, weight, address):
        self.lastname = lastname
        self.firstname = firstname
        self.weight = weight
        self.address = address
    def say_hello(self):
        pass

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
