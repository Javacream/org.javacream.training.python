
import shopping_list_module as slm
def main():
    raw_data = slm.read_raw_shopping_list()
    cleaned_data = slm.clean(raw_data)
    slm.create_shopping_list(cleaned_data)
    slm.calculate_number_of_people(cleaned_data)
    slm.group_items(cleaned_data)

main()    