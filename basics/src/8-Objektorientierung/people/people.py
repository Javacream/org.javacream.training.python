class Person:
    def __init__(self, id, lastname, firstname):
        #Constructor
        #self: Referenz auf das eben erzeugte Objekt
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
    def __str__(self):
        elements = []
        for key, value in self.__dict__.items():
            elements.append('{key}={value}'.format(key=key, value=value))
        return ', '.join(elements)

class Address:
    def __init__(self, city, street):
        self.street = street
        self.city = city
    def __str__(self):
        return 'Address: city=' + self.city + ", street=" + self.street

class PeopleService:
    def __init__(self):
        self.counter = 0
        self.people = {}
    def create_person(self, lastname, firstname):
        self.counter = self.counter + 1
        person = Person(self.counter, lastname, firstname)
        self.people[self.counter] = person
        return self.counter
    def find_person_by_id(self, id):
        return self.people.get(id)   
    def find_all(self):
        return self.people.values()   
    def find_by_lastname(self, lastname):
        return [person for person in self.people.values() if person.lastname == lastname]   
    def find_by_firstname(self, firstname):
        return [person for person in self.people.values() if person.firstname == firstname]   
    def find_by_city(self, city):
        return [person for person in self.people.values() if (hasattr(person, 'address')) and (person.address.city == city)]   

    def delete_by_id(self, id):
        self.people.pop(id)
    def update(self, person):
        self.people[person.id] = person
    def say_hello(self, person):
        template = "my name is {} {}"
        return template.format(person.firstname, person.lastname)
