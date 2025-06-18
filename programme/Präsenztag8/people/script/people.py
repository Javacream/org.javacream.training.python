import requests
import json
def read_people(endpoint):
    return requests.get(endpoint).json()

def male(people_data):
    return [person for person in people_data if person['gender'] == 'm']

def female(people_data):
    return [person for person in people_data if person['gender'] == 'f']

def diverse(people_data):
    return [person for person in people_data if person['gender'] == 'd']

def write_result(path, data):
    with open(path, 'wt', encoding='utf-8') as file:
        json.dump(data, file)
