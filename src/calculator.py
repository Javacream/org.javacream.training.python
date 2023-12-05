def main():
    
    condition = True

    while condition:

        # User input
        input_string = input("Input number1 or exit: ")
        if input_string == 'exit':
            #condition = False
            break
        else:    
            number1_as_string = input_string
            number2_as_string = input("Input number2: ")

            # Type conversion
            number1 = float(number1_as_string)
            number2 = float(number2_as_string)

            # sum
            sum = number1 + number2

            # console output
            #output_string = 'The sum of ' + number1_as_string + ' and ' + number2_as_string + ' is ' + str(sum)
            output_string = f'the sum of {number1} and {number2} is {sum}'
            print(output_string)

main()