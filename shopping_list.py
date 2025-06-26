path = 'data/raw_shopping_list.txt'
with open(path, 'rt', encoding='utf-8') as file:
    raw_rows = file.readlines()
rows = []
for raw_row in raw_rows:
    rows.append(raw_row.replace('\n', ''))
print(rows)
