import requests
import json

class Person:
    def __init__(self, id: int, lastname: str, firstname: str, gender: str, height: int):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.gender = gender
        self.height = height
    def __repr__(self):
        return f'Person(lastname={self.lastname}, firstname={self.firstname}, gender={self.gender}, height={self.height})'
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.id == other.id 
        else:
            return False
    def __hash__(self):
        return hash(self.id)
        
class PeopleService:
    def __init__(self, endpoint):
        self.endpoint = endpoint
    def read_people(self):
        people_data = requests.get(self.endpoint).json()
        self.people = list()
        for person_dict in people_data:
            self.people.append(Person(person_dict['id'], person_dict['lastname'], person_dict['firstname'], person_dict['gender'], person_dict['height']))

    def male(self):
        return [person for person in self.people if person.gender == 'm']

    def female(self):
        return [person for person in self.people if person.gender == 'f']

    def diverse(self):
        return [person for person in self.people if person.gender == 'd']
    def to_list_of_dict(self, list_of_people: list[Person]):
        return [{'id': person.id, 'lastname': person.lastname, 'firstname': person.firstname, 'gender': person.gender, 'height': person.height} for person in list_of_people]
    def write_result(self):
        path = 'result/male.json'
        with open(path, 'wt', encoding='utf-8') as file:
            json.dump(self.to_list_of_dict(self.male()), file)
        path = 'result/female.json'
        with open(path, 'wt', encoding='utf-8') as file:
            json.dump(self.to_list_of_dict(self.female()), file)
        path = 'result/diverse.json'
        with open(path, 'wt', encoding='utf-8') as file:
            json.dump(self.to_list_of_dict(self.diverse()), file)
