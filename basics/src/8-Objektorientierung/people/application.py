from people import PeopleService, Address

def main():
    def print_person_list(list):
        for person in list:
            print(str(person))

    people_service = PeopleService()
    id1 = people_service.create_person("Meier", "Hans")
    id2 = people_service.create_person("Schneider", "Hanna")
    id3 = people_service.create_person("Meier", "Korinna")
    a = Address('München', 'Marienplatz')
    people_service.find_person_by_id(id1).address = a
    print_person_list(people_service.find_all())
    print_person_list(people_service.find_by_lastname("Schneider"))
    print_person_list(people_service.find_by_firstname("Hans"))
    print_person_list(people_service.find_by_city("München"))
    people_service.delete_by_id(id2)
    print_person_list(people_service.find_all())


if __name__ == "__main__":
    main()