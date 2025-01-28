filename = './shopping_list.txt' 
with open(filename) as file:
    rows = file.readlines()
    print(rows)