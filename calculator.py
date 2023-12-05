def main():
    
    # User input
    number1_as_string = input("Input number1: ")
    number2_as_string = input("Input number2: ")

    # Type conversion
    number1 = float(number1_as_string)
    number2 = float(number2_as_string)

    # sum
    sum = number1 + number2

    # console output
    output_string = 'The sum of ' + number1_as_string + ' and ' + number2_as_string + ' is ' + str(sum)
    print(output_string)

main()