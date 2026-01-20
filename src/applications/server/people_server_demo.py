import requests

def load_people(url):
    response = requests.get(url)
    return response.json()
def get_tall_people(people):
    min_size = 190
    tall_people = [f'{person["firstname"]} {person["lastname"]}' for person in people if person['height'] >= min_size]
    return tall_people
def main():
    url = "http://javacream.eu:8080/people"
    people_data = load_people(url)
    print(get_tall_people(people_data))
main()