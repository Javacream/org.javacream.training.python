import shopping_list

def main():
    #path = "shopping_list.txt"
    rows = shopping_list.read_shopping_list()
    shopping_data = shopping_list.create_shopping_data(rows)
    shopping_list.write_shopping_data(shopping_data)
    print(f'Namensliste: {shopping_list.create_unique_names(shopping_data)}')
    print(f'Produktliste: {shopping_list.create_unique_products(shopping_data)}')
    print(f'Produktliste mit Anzahl: {shopping_list.create_products_amounts(shopping_data)}')
    print(f'Produktliste pro Person: {shopping_list.create_products_by_people(shopping_data)}')

main()