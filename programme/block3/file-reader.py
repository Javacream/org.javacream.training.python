try:
    with open('data/info.txt', encoding='utf-8') as file:
        content = file.read()
    print(content)
except Exception as e:
    print(e)