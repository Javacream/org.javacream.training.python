import json

def load_people(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)
    return response.json()
def get_tall_people(people):
    min_size = 190
    tall_people = [f'{person["firstname"]} {person["lastname"]}' for person in people if person['height'] >= min_size]
    return tall_people
