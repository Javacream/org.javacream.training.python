from people import Address, Person, PeopleService, Worker
# import people
def main():
    a1 = Address("München", "Marienplatz")
    a2 = Address("Berlin", "Alexanderplatz")
    person1: Person = Person("Sawitzki", 183, 75.7, a1)
    person2 = Person("Meier", 189, 83.5, a2)
    person3 = Person("Musterperson", 189, 63.5, a2)
    people_service = PeopleService()
    people_service.add(person1)
    people_service.add(person2)
    people_service.add(person3)
    people_with_height_189 = people_service.find_by_height(189)
    for person in people_with_height_189:
        print(person.name)
    w = Worker('Schufter', 183, 88.3, a2, 'Cegos')
    print("done")
main()