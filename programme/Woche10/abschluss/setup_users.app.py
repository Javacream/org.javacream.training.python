from setup_users import UsersSetup
from configuration import read_configuration
from people import PeopleService
def main():
    configuration = read_configuration('programme/Woche10/configuration.json')
    people_service = PeopleService(configuration['people_server']['endpoint'])
    people_json = people_service.get_people()
    client_setup = UsersSetup()
    client_setup.init(configuration)
    client_setup.setup()
    client_setup.create_remote_directories(people_json)
    client_setup.close()

if __name__ == '__main__':
    main()