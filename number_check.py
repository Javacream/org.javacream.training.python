def read_number():
    number_string = input("please enter a number: ")
    return int(number_string)

def check_number(number):
    result = (number > 10)
    return result

def check_even(number):
    rest = (number % 2)
    return  rest == 0

def print_result(greater_10, even):
    greater_10_string = str(greater_10)
    print("Entered number was greater than 10: " + greater_10_string)
    print("Entered number was even: " + str(even))

def main():
    number = read_number()
    greater_than_10 = check_number(number)
    even_number = check_even(number)
    print_result(greater_than_10, even_number)

main()    