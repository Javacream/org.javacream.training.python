def sum_elements(number_list: list[int]) -> int:
    result: int = 0
    for number in number_list:
        result = result + number
    return result

def main():
    list_of_numbers: list[int] = [1, 7, 19, -4]
    sum_of_numbers = sum_elements(list_of_numbers)
    print(sum_of_numbers)

main()