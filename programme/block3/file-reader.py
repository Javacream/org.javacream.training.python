try:
    file = open('data/info.txt', encoding='utf-8')
    content = file.read()
    file.close()
    print(content)
except Exception as e:
    print(e)