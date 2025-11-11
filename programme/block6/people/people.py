class Address:
    def __init__(self, city:str, street: str):
        self.city = city
        self.street = street
    def copy(self):
        return Address(self.city, self.street)
    
    def __eq__(self, other):
        if isinstance(other, Address):
            return (self.city == other.city) and (self.street == other.street)
        else:
            return False

class Person(object):
    def __init__(self, lastname: str, firstname: str, height: int, weight: float):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.weight = weight
        self.addresses = set()
    def __repr__(self):
        return f'Person(lastname={self.lastname}, firstname={self.firstname}, height={self.height}, weight={self.weight})'
    def __add__(self, add_weight):
        if isinstance(add_weight, float):
            self.weight += add_weight
            return self
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Person' and '{type(add_weight)}'")    
    def greet(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'

class Student(Person):
    def __init__(self, lastname: str, firstname: str, height: int, weight: float, university:str):
        super().__init__(lastname, firstname, height, weight)
        self.university = university
    def study(self):
        print(f'{self.lastname} studying at {self.university}')
    def greet(self):
        print('####')
        return f'{super().greet()}, i am a student'
