
from shopping_list_module import *
import fileutils as fu
def main():
    path = 'data/raw_shopping_list.txt'
    raw_data = fu.read_raw(path)
    cleaned_data = fu.clean(raw_data)
    create_shopping_list(cleaned_data)
    calculate_number_of_people(cleaned_data)
    group_items(cleaned_data)

if __name__ == '__main__':
    main()    