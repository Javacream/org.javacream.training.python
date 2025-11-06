class Address:
    def __init__(self, city:str, street: str):
        self.city = city
        self.street = street
    def copy(self):
        return Address(self.city, self.street)    
class Person:
    def __init__(self, lastname: str, firstname: str, height: int, weight: float, address: Address):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.weight = weight
        self.address = address.copy()
    def say_hello(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'

class Student(Person):
    def __init__(self, lastname: str, firstname: str, height: int, weight: float, address: Address, university: str):
        super().__init__(lastname, firstname, height, weight, address)        
        self.university = university
    
    def study(self):
        print(f'{self.lastname} is studying at {self.university}')

