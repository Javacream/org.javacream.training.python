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

class Student(Person):
    def __init__(self, lastname, firstname, university):
        super().__init__(lastname, firstname)
        self.university = university        
    def study(self):
        return f'{self.introduce()}, i am studying at {self.university}'