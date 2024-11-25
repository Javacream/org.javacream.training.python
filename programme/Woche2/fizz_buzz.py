number = 1
while number <= 30:
    dividable_by_three = False
    dividable_by_five = False
    if number % 3 == 0:
        dividable_by_three = True
    if number % 5 == 0:
        dividable_by_five = True

    if dividable_by_three and dividable_by_five:
        print('FizzBuzz')
    elif dividable_by_three:
        print('Fizz')
    elif dividable_by_five:
        print('Buzz')
    else:
        print(f'{number}')
    number += 1    

