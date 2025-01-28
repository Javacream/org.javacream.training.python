filename = './shopping_list.txt' 
with open(filename, encoding='utf-8') as file:
    rows = file.readlines()
    print(rows)