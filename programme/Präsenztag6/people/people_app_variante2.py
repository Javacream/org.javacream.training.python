from os import getcwd
from people import prepare, check_file_exists, read_lines, create_people_data, write_people_data

def main():
    file_name =  './data/people.csv'
    if check_file_exists(file_name):
        prepare()
        lines = read_lines(file_name)
        people_data = create_people_data(lines)
        write_people_data(people_data)
    else:
        print(f'input file {file_name} does not exist in {getcwd().replace('\\', '/')}')
    print('done')

main()