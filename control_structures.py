number1 = 42
number2 = 9

# if

if number1 > number2:
    print(f'{number1} is greater than {number2}')

# if - elif

if number1 < number2:
    print(f'{number1} is smaller than {number2}')
elif number1 > 2*number2:
    print(f'{number1} is greater than {2*number2}')

# if - else    

if number1 < number2:
    print(f'{number1} is smaller than {number2}')
else:
    print(f'{number1} is greater than {number2}')

index = 0
end = 5
while index < 5:
    print(f'Index={index}')
    # index = index + 1
    index += 1
    # index++ nicht in Python!

try:
    value = input('Bitte Zahl eingeben: ')
    value = float(value)
    print(f'the double of {value} = {2*value}')
except Exception as e:
    print(f'an error has occured: {e}')
