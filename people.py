import json

def main():
    with open ('people.json', 'rt', encoding='utf-8') as file:
        people_data_list = json.load(file)
    person1_data_dictionary = people_data_list[0]
    person1_lastname = person1_data_dictionary['lastname']
    print(person1_lastname)

    print('done')

main()