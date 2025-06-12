import file_util as fu
import people as p
import json

def main():
    lines = fu.read_lines('./data/people.csv')
    people_dictionary = p.create_people_data(lines)
    fu.write_json('./result/people.json', people_dictionary)
main()