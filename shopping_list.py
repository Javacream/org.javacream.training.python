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

def unique_names(shopping_data):
    uniques = {data[0] for data in shopping_data}
    return uniques
    
def main():
    path = "shopping_list.txt"
    rows = read_shopping_list(path)
    shopping_data = create_shopping_data(rows)
    write_shopping_data(shopping_data)
    print(unique_names(shopping_data))
main()