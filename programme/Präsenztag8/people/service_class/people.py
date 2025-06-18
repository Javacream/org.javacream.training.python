import requests
import json

class PeopleService:
    def __init__(self, endpoint):
        self.endpoint = endpoint
    def read_people(self):
        self.people_data = requests.get(self.endpoint).json()

    def male(self):
        return [person for person in self.people_data if person['gender'] == 'm']

    def female(self):
        return [person for person in self.people_data if person['gender'] == 'f']

    def diverse(self):
        return [person for person in self.people_data if person['gender'] == 'd']

    def write_result(self):
        path = 'result/male.json'
        with open(path, 'wt', encoding='utf-8') as file:
            json.dump(self.male(), file)
        path = 'result/female.json'
        with open(path, 'wt', encoding='utf-8') as file:
            json.dump(self.female(), file)
        path = 'result/diverse.json'
        with open(path, 'wt', encoding='utf-8') as file:
            json.dump(self.diverse(), file)
