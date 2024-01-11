def my_function():
    print('called my_function')

def my_function_with_one_param(p):
    print(f'called my_function_with_one_param, param={p}')

def my_function_with_return():
    print(f'called my_function_with_return')
    return 'OK'
def my_function_all_together(p1, p2):
    print(f'called my_function_all_togehther, param1={p1}, param2={p2}')
    return 'OK'
def my_function_complex(number1, number2):
    if number1 == number2:
        return True
    elif number1 > number2:
        return 'Greater'


def main():
    my_function()
    # my_function('Hugo) # my_function does not take a parameter
    result = my_function() # result is None, my_function does not return a value
    my_function_with_one_param('Hugo')
    # my_function_with_one_param() # parameter is mandatory
    # my_function_with_one_param('a', 'b') # too many parameters
    result = my_function_with_one_param('Hugo') # result is None
    result = my_function_with_return() # result is 'OK'
    result = my_function_all_together('this', 'that') # result is 'OK'
    result = my_function_complex(10, 10) # True
    result = my_function_complex(20, 10) # 'Greater'
    result = my_function_complex(2, 10) # None
    print('done')


main()


