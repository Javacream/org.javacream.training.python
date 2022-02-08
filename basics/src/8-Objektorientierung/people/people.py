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
    def say_hello(self, person):
        template = "my name is {} {}"
        return template.format(person.firstname, person.lastname)
