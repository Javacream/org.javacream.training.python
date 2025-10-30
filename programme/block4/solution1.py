def sum_elements(number_list):
    result = 0
    for number in number_list:
        result = result + number
    return result

def main():
    list_of_numbers = [1, 7, -5, 28]
    sum_of_list = sum_elements(list_of_numbers) # implizit wird hier intern ausgeführt: number_list = list_of_numbers
    print(sum_of_list)

main()