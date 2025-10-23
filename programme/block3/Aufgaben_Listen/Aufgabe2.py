numbers = [1, 6, -3, 91, 66, -2]

min_number = 999999999999999999
max_number = -min_number

for number in numbers:
    if number < min_number:
        min_number = number
    if (number > max_number):
        max_number = number

print(f'min: {min_number}, max: {max_number}')

print(f'min: {min(numbers)}, max: {max(numbers)}')
