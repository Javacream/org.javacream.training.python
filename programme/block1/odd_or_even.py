number = float(input('Bitte geben Sie eine Zahl ein: '))

rest = number % 2

if rest == 1:
    print(f'{number} is odd')
else:
    print(f'{number} is even')