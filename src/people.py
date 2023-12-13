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
