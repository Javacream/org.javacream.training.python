class Person:
    def __init__(self, lastname, firstname, weight, main_address, *addresses):
        self.lastname = lastname 
        self.firstname = firstname
        self.weight = weight
        self.main_address = main_address
        self.addresses = set(addresses)
    def say_hello(self):
        message = f"Hallo, mein Name ist {self.firstname} {self.lastname}"
        return message
    
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
    def get_address(self):
        return f'Addresse: {self.street}, {self.city}'