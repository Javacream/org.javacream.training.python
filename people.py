class Person:
    def __init__(self, lastname, firstname, *addresses):
        self.lastname = lastname
        self.firstname = firstname
        self.addresses = addresses # self.addresses ist ein Tuple
        #self.addresses = set(addresses)# self.addresses ist ein Tuple
    def introduce(self):
        return f'Hello, my name is {self.firstname} {self.lastname}'
    def __repr__(self):
        return f'Person(lastname={self.lastname}, firstname={self.firstname})'    


class Address:
    def __init__(self, city, street):
        self.street = street
        self.city = city
    def __eq__(self, other_address):
        if isinstance(other_address, Address):
            return (self.city == other_address.city) and (self.street == other_address.street) 
        else:
            return False
    def __hash__(self):
        return hash(self.city) + hash(self.street)
    def __repr__(self):
        return f'Address(city={self.city}, street={self.street})'    

class Student(Person):
    def __init__(self, lastname, firstname, university, *addresses):
        super().__init__(lastname, firstname, addresses)
        self.university = university
    def study(self):
        return f'{self.introduce()}, i am studying at {self.university}'        
class Worker(Person):
    def __init__(self, lastname, firstname, company, *addresses):
        super().__init__(lastname, firstname, addresses)
        self.company = company
    def work(self):
        return f'{self.introduce()}, i am working at {self.company}'    