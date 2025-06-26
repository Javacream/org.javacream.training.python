path = 'data/raw_shopping_list.txt'
with open(path, 'rt', encoding='utf-8') as file:
    raw_rows = file.readlines()
rows = [raw_row.replace('\n', '') for raw_row in raw_rows if raw_row.replace('\n', '').strip() != '']
print(rows)
