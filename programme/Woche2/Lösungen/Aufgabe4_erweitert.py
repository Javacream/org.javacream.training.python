start_number = input('Bitte geben Sie die Startzahl an: ')
start_number = int(start_number)
end_number = input('Bitte geben Sie die Endzahl an: ')
end_number = int(end_number)

first_divider = input('Bitte geben Sie den ersten Teiler an: ')
first_divider = int(first_divider)
second_divider = input('Bitte geben Sie den zweiten Teiler an: ')
second_divider = int(second_divider)

number = start_number

while number <= end_number:
    dividable_by_first = False
    dividable_by_second = False
    if number % first_divider == 0:
        dividable_by_first = True
    if number % second_divider == 0:
        dividable_by_second = True

    if dividable_by_first and dividable_by_second:
        print('FizzBuzz')
    elif dividable_by_first:
        print('Fizz')
    elif dividable_by_second:
        print('Buzz')
    else:
        print(f'{number}')
    number += 1    

