from people import create_person, find_person_by_id

def main():
    sawitzki_id = create_person("Sawitzki", "Rainer")
    meier_id = create_person("Meier", "Hanna")
    print(find_person_by_id(sawitzki_id))
    print(find_person_by_id(meier_id))
    print(find_person_by_id(42))

if __name__ == "__main__":
    main()