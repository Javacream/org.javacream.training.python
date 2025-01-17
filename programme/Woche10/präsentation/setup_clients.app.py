from setup_clients import ClientSetup
from configuration import read_configuration
from people import PeopleService
def main():
    configuration = read_configuration('programme/Woche10/präsentation/configuration.json')
    people_service = PeopleService(configuration['people_server']['endpoint'])
    people_json = people_service.get_people()
    client_setup = ClientSetup()
    client_setup.init(configuration)
    client_setup.setup()
    client_setup.create_remote_directories(people_json)
    client_setup.close()

if __name__ == '__main__':
    main()