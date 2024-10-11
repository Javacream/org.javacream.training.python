class Person:
    def __init__(self, lastname, firstname, address):
        self.companies = set()
class Address:
    def __init__(self, city, street):
        pass 
class Company:
    def __init__(self, name):
        self.employees = set()
class PeopleService:
    def __init__(self):
        self.people = set()
    def create(self, lastname, firstname, address):
        self.people.add(Person(lastname, firstname, address))
    def read(criteria):
        pass    
    def update(person):
        pass    
    def delete(person):
        pass
class AddressService:
    def __init__(self):
        self.addresses = set()
    def create(self, city, street):
        self.people.add(Address(city, street))
    def read(criteria):
        pass    
    def update(address):
        pass    
    def delete(address):
        pass
class CompanyService:
    def __init__(self):
        self.companies = set()        
    def create(self, name):
        self.people.add(Company(name))
    def read(criteria):
        pass    
    def update(company):
        pass    
    def delete(company):
        pass
