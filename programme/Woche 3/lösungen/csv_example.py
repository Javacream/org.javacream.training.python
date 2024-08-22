with open ('username.csv', 'r') as file:
    result = [row[0:len(row) - 1].split(';') for row in file.readlines()]
print(result)