path = 'data/raw_shopping_list.txt'
file = open(path, 'rt', encoding='utf-8')
content = file.read()
file.close()
print(content)