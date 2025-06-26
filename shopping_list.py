path = 'data/raw_shopping_list.txt'
with open(path, 'rt', encoding='utf-8') as file:
    content = file.read()
print(content)
