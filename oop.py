class Person:
    def __init__(self, lastname, firstname): # Konstruktor
        self.lastname = lastname
        self.firstname = firstname
        self.addresses = set()
    def introduce(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'
class Address(object):
    def __init__(self, city, street):
        self.city = city
        self.street = street
        self.people = list()
    def __repr__(self):
        return f'Address: city={self.city}, street={self.street}'
    def __eq__(self, other):
        return self.city.__eq__(other.city) and self.street.__eq__(other.street)
    def __hash__(self):
        return self.city.__hash__()

class Student(Person):
    def __init__(self, lastname, firstname, university):
        super().__init__(lastname, firstname)
        self.university = university        
    def study(self):
        return f'{self.introduce()}, i am studying at {self.university}'