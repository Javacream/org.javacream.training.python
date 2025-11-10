class Address:
    def __init__(self, city:str, street: str):
        self.city = city
        self.street = street
    def copy(self):
        return Address(self.city, self.street)
    def __repr__(self):
        return f'Address(city={self.city}, street={self.street})'
    def __eq__(self, other):
        if isinstance(other, Address):
            return (self.city == other.city) and (self.street == other.street)
        else:
            return False
class Person(object):
    def __init__(self, lastname: str, firstname: str, height: int, weight: float, address: Address):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.weight = weight
        self.address = address.copy()
    def say_hello(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'
    
    def __repr__(self):
        return f'Person(lastname={self.lastname}, firstname={self.firstname}, height={self.height}, weight={self.weight})'

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.height > other.height
        else:
            return False
class Student(Person):
    def __init__(self, lastname: str, firstname: str, height: int, weight: float, address: Address, university: str):
        super().__init__(lastname, firstname, height, weight, address)        
        self.university = university
    
    def study(self):
        print(f'{self.lastname} is studying at {self.university}')

    def say_hello(self):
        return f'{super().say_hello()}, i study at {self.university}'
