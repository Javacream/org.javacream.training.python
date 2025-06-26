class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname 
    def introduce(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'


class Address:
    def __init__(self, city, street):
        self.street = street
        self.city = city
