import os
import people

def main():
    file_name =  './data/people.csv'
    if people.check_file_exists(file_name):
        people.prepare()
        lines = people.read_lines(file_name)
        people_data = people.create_people_data(lines)
        people.write_people_data(people_data)
    else:
        print(f'input file {file_name} does not exist in {os.getcwd().replace('\\', '/')}')
    print('done')

main()