import requests

def main():
    people_data_list = requests.get('http://javacream.eu:8080/people').json()
    person1_data_dictionary = people_data_list[0]
    person1_lastname = person1_data_dictionary['lastname']
    print(person1_lastname)

    print('done')

main()