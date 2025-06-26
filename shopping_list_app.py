
import shopping_list_module
def main():
    raw_data = shopping_list_module.read_raw_shopping_list()
    cleaned_data = shopping_list_module.clean(raw_data)
    shopping_list_module.create_shopping_list(cleaned_data)
    shopping_list_module.calculate_number_of_people(cleaned_data)
    shopping_list_module.group_items(cleaned_data)

main()    