def main():
    
    while True:

        # User input
        input_string = input("Input number1 or exit: ")
        if input_string.lower() == 'exit':
            break
        else:    
            number1_as_string = input_string
            number2_as_string = input("Input number2: ")
            if number1_as_string.replace(".", "").isnumeric() and number2_as_string.replace(".", "").isnumeric():
                number1 = float(number1_as_string)
                number2 = float(number2_as_string)
                while True:
                    operation = input("enter operation (plus, minus, multiply, divideby): ")
                    if (operation == "plus"):
                        result = number1 + number2
                        operation_message = "plus"
                        break
                    elif (operation == "minus"):
                        result = number1 - number2
                        operation_message = "minus"
                        break
                    elif (operation == "multiply"):
                        result = number1 * number2
                        operation_message = "times"
                        break
                    elif (operation == "divideby"):
                        result = number1 / number2
                        operation_message = "divided by"
                        break
                    else:
                        print(f"invalid operation: {operation}")
                output_string = f'{number1} {operation_message} {number2} is {result}'
                print(output_string)
            else:
                print(f'invalid number, you entered {number1_as_string}, {number2_as_string}')    

main()