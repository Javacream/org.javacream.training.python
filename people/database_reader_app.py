from database_people_service import PeopleService
from fileutil import write_json_data
def main():
    config = {
        'host': 'javacream.eu',
        'port': 3406,
        'database': 'javacream',
        'user': 'user',
        'password': 'user'
    }
    people_service = PeopleService(config)
    people = people_service.read_people()
    people_data = [{'id': person.id, 'lastname': person.lastname, 'firstname': person.firstname, 'gender': person.gender, 'height': person.height} for person in people]
    write_json_data('data/people_from_database.json', people_data)

if __name__ == '__main__':
    main()