class Person:
    def __init__(self, lastname: str, firstname: str, weight: float, height: int):
        self.lastname = lastname
        self.firstname = firstname
        self.weight = weight
        self.height = height
        self.addresses: list[Address] = list()
    def say_hello(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'
    

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street