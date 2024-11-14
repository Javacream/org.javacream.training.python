class Person:
    def __init__(self, lastname, firstname): # Konstruktor
        self.lastname = lastname
        self.firstname = firstname
        self.addresses = set()
    def introduce(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
        self.people = list()