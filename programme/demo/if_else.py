number1 = input("Bitte geben Sie die erste Zahl an: ")
number2 = input("Bitte geben Sie die zweite Zahl an: ")

number1 = float(number1)
number2 = float(number2)

if number1 > number2:
    print(f'{number1} is greater than {number2}')
else:
    print(f'{number1} is less or equal {number2}')
