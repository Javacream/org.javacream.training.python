number1 = input("Bitte geben Sie die erste Zahl an: ")
number2 = input("Bitte geben Sie die zweite Zahl an: ")

number1 = float(number1)
number2 = float(number2)

sum = number1 + number2
print(f'Die Summe aus {number1} und {number2} = {sum}')

diff = number1 - number2

print(f'Die Differenz von {number1} und {number2} = {diff}')

print(f'Das Produkt von {number1} und {number2} = {number1 * number2}')
print(f'Der Quotient von {number1} und {number2} = {number1 / number2}')

print(f'Ist {number1} größer als {number2} = {number1 > number2}')
