import bmi as bmi_module 
import people_data
import os
def main():
    indir = 'Tag5/testing/bmi/data'
    outdir = 'Tag5/testing/bmi/result'
    infiles = os.listdir(indir)
    data_counter = 0
    people_in_categories = dict()
    people_in_categories['untergewichtig'] = []
    people_in_categories['normalgewichtig'] = []
    people_in_categories['übergewichtig'] = []
    people_in_categories['fettleibig'] = []
    people_by_gender = {'m':[], 'w': [], 'd':[]}
    for infilename in infiles:
        people_list = people_data.read_person_data(f'{indir}/{infilename}')
        for person in people_list:
            bmi = bmi_module.calculate_bmi(person.height, person.weight)
            bmi_category = bmi_module.bmi_category_for(bmi)
            people_in_categories[bmi_category].append(person)
            people_by_gender[person.gender].append(f'{person.name} ist {bmi_category}')
            data_counter += 1
    for gender in people_by_gender:
        people_data.write_person_data(f'{outdir}/{infilename}.{gender}.txt', people_by_gender[gender])    
    print(f'Anzahl gelesener Personendaten: {data_counter}')
    for category in people_in_categories:
        print(f'In der Kategorie {category} sind {len(people_in_categories[category])} Personen')
    print(f'Anzahl gelesener Personendaten: {data_counter}')
if __name__ == '__main__':
    main()


