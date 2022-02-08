import people

cp = people.create_person
fp = people.find_person_by_id

def main():
    sawitzki_id = cp("Sawitzki", "Rainer")
    meier_id = cp("Meier", "Hanna")
    print(fp(sawitzki_id))
    print(fp(meier_id))
    print(fp(42))

if __name__ == "__main__":
    main()