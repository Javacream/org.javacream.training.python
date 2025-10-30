import json
def parse_people():
    with open('data/people.json', encoding='utf-8') as file:
        people_data = json.load(file)
    return people_data

def main():
    people = parse_people()
    print(people)

main()