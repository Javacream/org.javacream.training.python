class Person:
    def __init__(self, lastname, firstname, *addresses):
        self.lastname = lastname
        self.firstname = firstname
        self.addresses = addresses # self.addresses ist ein Tuple
        #self.addresses = set(addresses)# self.addresses ist ein Tuple
    def introduce(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'


class Address:
    def __init__(self, city, street):
        self.street = street
        self.city = city
