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
            try:
                number1 = float(number1_as_string)
                number2 = float(number2_as_string)
                operation = input("enter operation (plus, minus, multiply, divideby)")
                if (operation == "plus"):
                    result = number1 + number2
                    operation_message = "plus"
                elif (operation == "minus"):
                    result = number1 - number2
                    operation_message = "minus"
                elif (operation == "multiply"):
                    result = number1 * number2
                    operation_message = "times"
                elif (operation == "divideby"):
                    result = number1 / number2
                    operation_message = "divided by"
                else:
                    print(f"invalid operation: {operation}")
                    continue # dieses continue ist notwendig, sonst erfolgt eine sinnlose Ausgabe
                # console output
                #output_string = 'The sum of ' + number1_as_string + ' and ' + number2_as_string + ' is ' + str(sum)
                output_string = f'{number1} {operation_message} {number2} is {result}'
                print(output_string)
            except:
                print(f'invalid number, you entered {number1_as_string}, {number2_as_string}')    
                continue # in diesem Beispiel eigentlich unnötig, da wir uns eh am Ende der while-Schleife befinden

main()