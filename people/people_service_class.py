import requests

class PeopleService:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def read_people(self):
        response = requests.get(self.endpoint)
        if response.status_code == 200:
            data = response.json()
            people = [Person(element['id'], element['lastname'], element['firstname'], element['height'], element['gender']) for element in data]
            return people
        
class Person:
    def __init__(self, id, lastname, firstname, height, gender):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.gender = gender
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.id == other.id
        else:
            return False
    def __hash__(self):
        return self.id
    def __repr__(self):
        return f'Person(id={self.id}, lastname={self.lastname}, firstname={self.firstname}, gender={self.gender}, height={self.height})'