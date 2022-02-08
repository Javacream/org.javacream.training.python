import people

def main():
    sawitzki_id = people.create_person("Sawitzki", "Rainer")
    meier_id = people.create_person("Meier", "Hanna")
    print(people.find_person_by_id(sawitzki_id))
    print(people.find_person_by_id(meier_id))
    print(people.find_person_by_id(42))

if __name__ == "__main__":
    main()