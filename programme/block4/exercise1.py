def sum_elements(number_list):
    result = 0
    for number in number_list:
        result = result + number
    return result

list_of_numbers = [1, 7, 19, -4]
sum_of_numbers = sum_elements(list_of_numbers)
print(sum_of_numbers)