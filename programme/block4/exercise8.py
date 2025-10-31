import json

def read_people_json(path):
    with open(path, encoding='utf-8') as file:
        return json. load(file)

def main():
    path = 'data/people.json'
    people_data = read_people_json(path)
    print(people_data)


main()