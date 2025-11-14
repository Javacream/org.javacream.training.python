path = 'data/people.txt'
people_file = open(path, encoding='utf-8')
content = people_file.read()
rows = content.split('\n')
people_file.close()
print(rows)