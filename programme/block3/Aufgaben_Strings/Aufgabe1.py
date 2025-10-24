string = 'Hello World!'

result = ''
string_length = len(string)
r = range(string_length - 1, -1, -1)
for index in r:
    character = string[index]
    result = result + character
print(result)

result = ''.join(reversed(string)) # join fügt pro element in dem reversed iterator ein Element hinzu
print(result)

result = string[::-1]
print(result)
