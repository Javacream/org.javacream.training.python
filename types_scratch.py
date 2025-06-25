number1 = 2.0
number2 = 22

result = number1 + number2
print(result)

firstname = 'Hugo'
lastname = ' Musterperson'

result = firstname + lastname
print(result)

print(type(number1))
print(type(firstname))

# result = number1 + lastname
result = number2*firstname
print(result)

age = 42.314159
name = 'Hugo'

# print(name + ' ist ' + age + ' Jahre alt')
print(name + ' ist ' + str(age) + ' Jahre alt') # Funktioniert, ist aber fürchterlich zu schreiben
print(f'{name} ist {age:.1f} Jahre alt')