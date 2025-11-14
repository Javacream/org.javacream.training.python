path = 'data/people.txt'
people_file = open(path, encoding='utf-8')
content = people_file.read()
people_file.close()
print(content)