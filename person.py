import sys

class Address:
    def __init__(self, postal_code, city, street):
        self.postal_code = postal_code
        self.city = city
        self.street = street
    def __str__(self):
        str_template = "Address: postalCode={}, city={}, street={}"
        return str_template.format(self.postal_code, self.city, self.street)
class Person(object): #(object) ist ab Python 3.x Standard, Die Klasse Person erbt von Object
    number_of_eyes = 2
    created_people = 0
    str_template = "Person: lastname={}, firstname={}, height={}, weight={}"
    def __init__(self, lastname, firstname, height, weight): # Constructor
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.weight = weight
        Person.created_people += 1
    def say_hello(self):
        return "Hi, my name is " + self.lastname
    def __str__(self):
        return Person.str_template.format(self.lastname, self.firstname, self.height, self.weight)
    def __repr__(self):
        return self.__str__()

class PeopleManager:
    def __init__(self):
        self.people = {}
        self.people_counter = 0
        self.__load_people__()
    def find_by_id(self, id):
        return self.people.get(id)    

    def find_by_lastname(self, lastname):
        return [person for person in self.people.values() if person.lastname == lastname]
    def find_by_firstname(self, firstname):
        return [person for person in self.people.values() if person.firstname == firstname]
    def find_heavier_than(self, min_weight):
        return [person for person in self.people.values() if person.weight >= min_weight]
    def find_by_height_range(self, min_height, max_height):
        return [person for person in self.people.values() if person.height > min_height and person.height < max_height]

    def create(self, lastname, firstname, height=176, weight=81):
        if (type(height) is str):
            height = int(height)
        if (type(weight) is str):
            weight = int(weight)
        self.people_counter = self.people_counter + 1 # shorter: self.people_counter += 1, ++ not in Python
        new_person = Person(lastname, firstname, height, weight)
        self.people[self.people_counter] = new_person
    def __load_people__(self):
        with open("people.txt", "r") as file:
            for row in file:
                if row.endswith('\n'):
                    row = row[0:len(row)-1]
                data =row.split(",")
                self.create(*data)

def write_result(filename, people):
    with open(filename, 'w') as file:
        for person in people:
            file.write(str(person) + '\n')


