numbers = [1, 42, -7, 9]

sum_of_numbers = 0
for number in numbers:
    sum_of_numbers += number
print(f'Summe ist {sum_of_numbers}')    

sum_of_numbers = sum(numbers)
print(f'Summe ist {sum_of_numbers}')    


def my_sum (collection):
    sum_of_numbers = 0
    for number in collection:
        sum_of_numbers += number
    return sum_of_numbers

sum_of_numbers = my_sum(numbers)
print(f'Summe ist {sum_of_numbers}')    
