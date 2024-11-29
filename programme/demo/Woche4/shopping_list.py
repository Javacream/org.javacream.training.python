# Unser Shopping-List-Beispiel

def read_raw_shopping_list():
    path = './programme/demo/Woche4/raw_shopping_list.txt'
    with open (path) as file:
        raw_items = file.readlines()
    return raw_items

def create_shopping_list(items = ['Apfel', 'Birne', 'Apfel']):
    unique_items = set(items)
    shopping_list = {item: items.count(item) for item in unique_items}
    return shopping_list

def write_shopping_list(shopping_list):
    path = './programme/demo/Woche4/shopping_list.txt'
    with open (path, 'wt') as file:
        for item in shopping_list:
            file.write(f'{item}: {shopping_list[item]}\n')
def main():
    raw_shopping_list = read_raw_shopping_list()
    shopping_list = create_shopping_list(raw_shopping_list) # Damit wird der Parameter items gesetzt / überschrieben
    write_shopping_list(shopping_list)

main()

