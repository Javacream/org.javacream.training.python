def read_number():
    number_string = input("please enter a number: ")
    return int(number_string)

def check_number(number):
    result = (number > 10)
    return result

def check_equal(number):
    return (number % 2) == 0

def print_result(greater_10, equal):
    print("Entered number was greater than 10: " + str(greater_10))
    print("Entered number was equal: " + str(equal))

def main():
    number = read_number()
    greater_than_10 = check_number(number)
    equal_number = check_equal(number)
    print_result(greater_than_10, equal_number)

main()    