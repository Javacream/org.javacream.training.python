from people_services import load_people, get_tall_people
def main():
    url = "src/applications/server/people.json"
    people_data = load_people(url)
    print(get_tall_people(people_data))

if __name__ == '__main__':
    main()