def sum_of_numbers(numbers):
    result = sum(numbers)
    return result

numbers_list = [2,3,4,5,6]
result_sum_of_numbers = sum_of_numbers(numbers_list) 
# implizit: numbers = numbers_list
# implizit, falls ein return angegeben ist: result_sum_of_numbers = result
print(result_sum_of_numbers)
