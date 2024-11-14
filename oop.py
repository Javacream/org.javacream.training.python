class Person:
    def __init__(self, lastname, firstname, address): # Konstruktor
        self.lastname = lastname
        self.firstname = firstname
        self.address = address
    def introduce(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street