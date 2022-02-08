from people import PeopleService, Address

def main():
    people_service = PeopleService()
    id1 = people_service.create_person("Meier", "Hans")
    id2 = people_service.create_person("Schneeider", "Hanna")
    a = Address('München', 'Marienplatz')
    p1 = people_service.find_person_by_id(id1)
    p1.address = a
    print(people_service.say_hello(p1))
    print(str(p1))

if __name__ == "__main__":
    main()