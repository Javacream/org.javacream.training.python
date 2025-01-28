filename = './shopping_list.txt' 
with open(filename, encoding='utf-8') as file:
    rows = file.readlines()
    cleaned_rows = [row[:-1] for row in rows if not row == '\n']
    shopping_set = set(cleaned_rows)
    print(shopping_set)