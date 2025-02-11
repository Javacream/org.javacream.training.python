import bmi as bmi_module 
import people_data
import os
def main():
    indir = 'Tag5/testing/bmi/data'
    outdir = 'Tag5/testing/bmi/result'
    infiles = os.listdir(indir)
    for infilename in infiles:
        people_list = people_data.read_person_data(f'{indir}/{infilename}')
        for person in people_list:
            people_data.categorize(person)
    for gender in people_data.people_by_gender:
        people_data.write_person_data(f'{outdir}/{infilename}.{gender}.txt', people_data.people_by_gender[gender])    
    print(f'Anzahl gelesener Personendaten: {people_data.data_counter}')
    for category in people_data.people_in_categories:
        print(f'In der Kategorie {category} sind {len(people_data.people_in_categories[category])} Personen')
    print(f'Anzahl gelesener Personendaten: {people_data.data_counter}')
if __name__ == '__main__':
    main()


