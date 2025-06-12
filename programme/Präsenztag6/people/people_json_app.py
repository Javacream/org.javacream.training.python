import os
import people
import file_util as fu
import sys
def application():
    print(sys.argv)
    file_name =  sys.argv[1] # './data/people.json'
    if fu.check_file_exists(file_name):
        people.prepare()
        people_data = fu.read_json(file_name)
        people_result = people.create_people_result(people_data)
        people.write_people_data(people_result)
    else:
        print(f'input file {file_name} does not exist in {os.getcwd().replace('\\', '/')}')
    print('done')

print(__name__)
if __name__ == '__main__':
    application()