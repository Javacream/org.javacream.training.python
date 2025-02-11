import bmi as bmi_module 
import people_data

def main():
    indir = 'Tag5/testing/bmi/data'
    outdir = 'Tag5/testing/bmi/result'

    infilename = input('Eingabedatei aus data-Verzeichnis: ')
    outfilename = input('Ausgabedatei in result-Verzeichnis: ')
    people_list = people_data.read_person_data(f'{indir}/{infilename}')
    people_result = list()
    for person in people_list:
        bmi = bmi_module.calculate_bmi(person.height, person.weight)
        bmi_category = bmi_module.bmi_category_for(bmi)
        people_result.append(f'{person.name} ist {bmi_category}')
    people_data.write_person_data(f'{outdir}/{outfilename}', people_result)    
if __name__ == '__main__':
    main()


