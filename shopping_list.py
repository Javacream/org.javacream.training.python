filename = './shopping_list.txt' 
with open(filename, encoding='utf-8') as file:
    rows = file.readlines()
    rows_without_eol = []
    for row in rows:
        if not row == '\n':
            row_without_eol = row[:-1]
            rows_without_eol.append(row_without_eol)
    print(rows_without_eol)