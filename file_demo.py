with open('./data/data1.txt', 'rt') as file:
    content = file.readlines()
    for row in content:
        if row.endswith('\n'):
            print(row[0:-1])
        else:
            print(row)
