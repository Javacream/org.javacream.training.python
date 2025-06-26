try:
    path = 'data/raw_shopping_list.txt'
    file = open(path, 'rt', encoding='utf-8')
    content = file.read()
    print(content)
except:
    print('something went wrong')
finally:
    if file:
        file.close()
