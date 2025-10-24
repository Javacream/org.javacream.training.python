try:
    with open('data/info.txt', encoding='utf-8') as file:
        content = file.readlines()
    for raw_todo in content:
        todo = raw_todo.replace('\n', '')
        print(todo)
except Exception as e:
    print(e)