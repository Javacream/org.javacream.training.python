path = 'data/raw_shopping_list.txt'
file = open(path)
content = file.read()
file.close()
print(content)