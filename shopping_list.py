def read_shopping_list(path):
    with open(path, 'rt', encoding='utf-8') as file:
        raw_rows = file.readlines()
    rows = [raw_row.replace('\n', '') for raw_row in raw_rows]
    return rows

def create_shopping_data(data_list):
    shopping_data = [(data.split(" ")[0], data.split(" ")[1], int(data.split(" ")[2])) for data in data_list]
    return shopping_data

def write_shopping_data(shopping_data):
    print(shopping_data)

def create_unique_names(shopping_data):
    uniques = {data[0] for data in shopping_data}
    return uniques

def create_unique_products(shopping_data):
    uniques = {data[1] for data in shopping_data}
    return uniques

def create_products_amounts(shopping_data):
    products = create_unique_products(shopping_data)
    products_amount = dict()
    for product in products:
        products_amount[product] = 0
    for data in shopping_data:
        product = data[1]
        amount = data[2]
        old_amount = products_amount[product]
        products_amount[product] = old_amount + amount
    return products_amount

def create_products_by_people(shopping_data):
    people = create_unique_names(shopping_data)
    products_by_people = {person : set() for person in people}
    for data in shopping_data:
        products_by_people[data[0]].add(data[1])
    return products_by_people    
def main():
    path = "shopping_list.txt"
    rows = read_shopping_list(path)
    shopping_data = create_shopping_data(rows)
    write_shopping_data(shopping_data)
    print(f'Namensliste: {create_unique_names(shopping_data)}')
    print(f'Produktliste: {create_unique_products(shopping_data)}')
    print(f'Produktliste mit Anzahl: {create_products_amounts(shopping_data)}')
    print(f'Produktliste pro Person: {create_products_by_people(shopping_data)}')

main()