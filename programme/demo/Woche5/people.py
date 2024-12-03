class Person:
    def __init__(self, lastname, firstname, weight, address):
        self.lastname = lastname 
        self.firstname = firstname
        self.weight = weight
        self.address = address
        address.inhabitants.append(self)
    def say_hello(self):
        message = f"Hallo, mein Name ist {self.firstname} {self.lastname}"
        return message
    
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
        self.inhabitants = list()
    def get_address(self):
        return f'Addresse: {self.street}, {self.city}'
    
class Company:
    def __init__(self, name):
        self.name = name
        self.addresses = set()

    
class Student(Person):
    def __init__(self, lastname, firstname, weight, address, uni):
        super().__init__(lastname, firstname, weight, address)
        self.university = uni

    def study(self):
        return f'Ich studiere'