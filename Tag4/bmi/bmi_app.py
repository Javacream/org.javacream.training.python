import bmi as bmi_module 
import people_data

def main():
    infile = 'Tag4/bmi/people.csv'
    outfile = 'Tag4/bmi/people_result.txt'

    people_list = people_data.read_person_data(infile)
    people_result = list()
    for person in people_list:
        name = person['name']
        height = person['height']
        weight = person['weight']
        bmi = bmi_module.calculate_bmi(height, weight)
        bmi_category = bmi_module.bmi_category_for(bmi)
        people_result.append(f'{name} ist {bmi_category}')
    people_data.write_person_data(outfile, people_result)    
if __name__ == '__main__':
    main()


