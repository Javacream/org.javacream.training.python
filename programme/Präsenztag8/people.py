class Person:
    def __init__(self, lastname: str, firstname: str, weight: float, height: int):
        self.lastname = lastname
        self.firstname = firstname
        self.weight = weight
        self.height = height
        self.addresses: list[Address] = list()
        print(f'***** erzeuge die Person {lastname}' )
    def say_hello(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'
    

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

class Student(Person):
    def __init__(self, lastname: str, firstname: str, weight: float, height: int, university):
        super().__init__(lastname, firstname, weight, height)
        self.university = university
    def study(self):
        return f'{self.say_hello()}, i am studying at {self.university}'
    
class Worker(Person):
    def __init__(self, lastname: str, firstname: str, weight: float, height: int, company):
        super().__init__(lastname, firstname, weight, height)
        self.company = company
    def work(self):
        return f'{self.say_hello()}, i am working at {self.company}'