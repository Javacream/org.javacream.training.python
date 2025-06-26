
from shopping_list_module import *
def main():
    raw_data = read_raw_shopping_list()
    cleaned_data = clean(raw_data)
    create_shopping_list(cleaned_data)
    calculate_number_of_people(cleaned_data)
    group_items(cleaned_data)

main()    