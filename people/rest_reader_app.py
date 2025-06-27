from rest_people_service import PeopleService
from fileutil import write_json_data
def main():
    people_service = PeopleService('http://javacream.eu:8080/people')
    people = people_service.read_people()
    write_json_data('data/people.json', people)

if __name__ == '__main__':
    main()