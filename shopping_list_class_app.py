
from shopping_list_class import ShoppingListService
import fileutils as fu
def main():
    path = 'data/raw_shopping_list.txt'
    raw_data = fu.read_raw(path)
    cleaned_data = fu.clean(raw_data)
    sls = ShoppingListService()
    sls.create_shopping_list(cleaned_data)
    sls.calculate_number_of_people(cleaned_data)
    sls.group_items(cleaned_data)

if __name__ == '__main__':
    main()    