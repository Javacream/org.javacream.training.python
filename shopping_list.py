path = 'data/raw_shopping_list.txt'
with open(path, 'rt', encoding='utf-8') as file:
    raw_rows = file.readlines()
rows = []
for raw_row in raw_rows:
    cleaned_row = raw_row.replace('\n', '')
    if cleaned_row.strip() != '':
        rows.append(cleaned_row)
print(rows)
