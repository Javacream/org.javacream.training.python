class Address:
    def __init__(self, city:str, street: str):
        self.city = city
        self.street = street
    def copy(self):
        return Address(self.city, self.street)

class Person:
    def __init__(self, lastname: str, firstname: str, height: int, weight: float):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.weight = weight
        self.addresses = set()

        
