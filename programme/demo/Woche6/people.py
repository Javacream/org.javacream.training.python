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
    def __repr__(self):
        return f'Person: lastname={self.lastname}, firstname={self.firstname}, weight={self.weight}, address={self.address}'
    
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
        self.inhabitants = list()
    def __eq__(self, other):
        if isinstance(other, Address):
            return (self.city == other.city) and (self.street == other.street)
        else:
            return False
    def __hash__(self):
        return hash(self.city) + hash(self.street)
    def __repr__(self):
        '''
        Vorsicht: Wenn hier die Inhabitants ausgegeben werden hätten wir eine Endlos-Rekursion,
        die zum Glück von Python erkannt wird. Trotzdem aufpassen! 
        '''
        return f'Address: {self.street}, {self.city}, inhabitants={self.inhabitants}' 
    
class Company:
    def __init__(self, name):
        self.name = name
        self.addresses = set()
    def __repr__(self):
        return f'Company: {self.name}, {self.addresses}'

    
class Student(Person):
    def __init__(self, lastname, firstname, weight, address, uni):
        super().__init__(lastname, firstname, weight, address)
        self.university = uni

    def say_hello(self):
        message = super().say_hello()
        return f"{message}, ich studiere"
    def study(self):
        return f'{super().say_hello()} studierend an der Universität {self.university}' 
