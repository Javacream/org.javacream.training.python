try:
    number1= input('Bitte erste Zahl eingeben: ')
    number2= input('Bitte zweite Zahl eingeben: ')
    number1 = int(number1)
    number2 = int(number2)
except Exception as e:
    print(e)

print('done')