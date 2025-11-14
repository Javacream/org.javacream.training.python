path = 'data/people.txt'
with open(path, encoding='utf-8') as people_file:
    content = people_file.read()
rows = content.split('\n')
print(rows)