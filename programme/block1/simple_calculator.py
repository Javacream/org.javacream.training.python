number1 = float(input('Bitte geben Sie eine Zahl ein: '))
number2 = float(input('Bitte geben Sie eine weitere Zahl ein: '))

# sum = number1+ number2 # sum ist eine BuiltIn-Function

sum_result = number1 + number2

print('Die Summe von ' + str(number1) + ' und ' + str(number2) + ' ist ' + str(sum_result))

difference_result = number1 - number2

print(f'Die Differenz von {number1} und {number2} ist {difference_result:.2f}')

print(f'Das Produkt von {number1} und {number2} ist {(number1 * number2):.2f}')

print(f'Der Quotient von {number1} und {number2} ist {(number1 / number2):.2f}')
