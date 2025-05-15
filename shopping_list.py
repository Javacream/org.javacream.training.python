def read_shopping_list(path):
    with open(path, 'rt', encoding='utf-8') as file:
        raw_rows = file.readlines()
        rows = []
        for raw_row in raw_rows:
            rows.append(raw_row.replace('\n', ''))
    return rows

def create_shopping_data(data_list):
    shopping_data = []
    for data in data_list:
        splitted = data.split(" ")
        data_tuple = (splitted[0], splitted[1], int(splitted[2]))
        shopping_data.append(data_tuple)
    return shopping_data

def write_shopping_data(shopping_data):
    print(shopping_data)

def main():
    path = "shopping_list.txt"
    rows = read_shopping_list(path)
    shopping_data = create_shopping_data(rows)
    write_shopping_data(shopping_data)

main()