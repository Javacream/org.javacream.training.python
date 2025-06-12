import os
import people
import file_util as fu

def application():
    file_name =  './data/people.csv'
    if fu.check_file_exists(file_name):
        people.prepare()
        lines = fu.read_lines(file_name)
        people_data = people.create_people_data(lines)
        people_result = people.create_people_result(people_data)
        people.write_people_data(people_result)
    else:
        print(f'input file {file_name} does not exist in {os.getcwd().replace('\\', '/')}')
    print('done')

print(__name__)
if __name__ == '__main__':
    application()