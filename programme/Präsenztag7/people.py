class Person:
    def __init__(self, lastname, firstname, weight, height, address):
        self.lastname = lastname
        self.firstname = firstname
        self.weight = weight
        self.height = height
        self.address = address
    def say_hello(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'
    

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street