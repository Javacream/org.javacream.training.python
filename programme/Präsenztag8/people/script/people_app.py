from people import *
def main():
    endpoint = 'http://javacream.eu:8080/people'
    people_data = read_people(endpoint)
    male_people = male(people_data)
    female_people = female(people_data)
    diverse_people = diverse(people_data)
    write_result('result/male.json', male_people)
    write_result('result/female.json', female_people)
    write_result('result/diverse.json', diverse_people)
if __name__ == '__main__': 
    main()