from people import PeopleService
def main():
    endpoint = 'http://javacream.eu:8080/people'
    people_service = PeopleService(endpoint)
    people_service.read_people()
    people_service.write_result()
if __name__ == '__main__': 
    main()