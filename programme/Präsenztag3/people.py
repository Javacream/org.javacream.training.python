with open('./programme/Präsenztag3/people.csv', 'rt', encoding='utf-8') as people_csv_file:
    rows = people_csv_file.read().splitlines()

for actual_row in rows:
    list_of_person_data = actual_row.split(',')  
    # print(f'{list_of_person_data[0]} {list_of_person_data[1]} ist {float(list_of_person_data[2])}kg schwer und {int(list_of_person_data[3])} cm groß')
    firstname = list_of_person_data[0]
    lastname = list_of_person_data[1]
    weight = float(list_of_person_data[2])
    height = int(list_of_person_data[3])
    print(f'{firstname} {lastname} ist {weight}kg schwer und {height} cm groß')
print('done')