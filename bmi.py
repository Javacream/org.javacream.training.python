import mysql.connector

def read_people_data():
    host = 'javacream.eu'
    port = 3406
    database = 'javacream'
    username = 'user'
    password = 'user'

    with mysql.connector.connect(host=host, port=port, database=database, username=username, password=password) as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT lastname, height*100, weight FROM PEOPLE')
        people_data_list = cursor.fetchall()
    return people_data_list

def calculate_bmi(height, weight):
     return weight /(height*height) * 10000

def categorize_bmi(bmi):
    if bmi < 18:
        bmi_category = 'underweight'
    elif bmi < 25:
        bmi_category = 'normalweight'
    elif bmi < 30:
        bmi_category = 'overweight'
    else:
        bmi_category = 'obese'
    return bmi_category

def print_bmi(name, bmi_category):
    with open ('people_bmi.txt', 'a', encoding='utf-8') as file:
        file.write(f'the person {name} is {bmi_category}\n')

def main():
    people_data = read_people_data()
    for person_data in people_data:
        name = person_data[0]
        height = person_data[1]
        weight = person_data[2]
        body_mass_index = calculate_bmi(height, weight)
        bmi_category = categorize_bmi(body_mass_index)
        print_bmi(name, bmi_category)

main()