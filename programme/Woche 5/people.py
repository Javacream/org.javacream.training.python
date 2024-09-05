class Address:
    def __init__(self, city, street) -> None:
        self.city = city
        self.street = street

class Person:
    def __init__(self, lastname:str, firstname:str, height:int, address: Address):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.addresses = []
        self.addresses.append(address)
    def say_hello(self) -> str: 
        return f'Hello, my name is {self.firstname} {self.lastname}'    
