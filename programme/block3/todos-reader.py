try:
    with open('data/info.txt', encoding='utf-8') as file:
        content = file.read()
    todos = content.split('\n')
    for todo in todos:
        print(todo)
except Exception as e:
    print(e)