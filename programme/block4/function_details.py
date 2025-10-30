def sum_elements(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def sum_elements_varargs(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def sum_elements_varargs_with_param(offset, *numbers):
    result = offset
    for number in numbers:
        result += number
    return result

def sum_elements_param_with_varargs(*numbers, offset):
    result = offset
    for number in numbers:
        result += number
    return result


def main():
    values = (1, 6, 4, 8)
    print(sum_elements(values))
    print(sum_elements_varargs(1, 6, 4, 8))
    print(sum_elements_varargs_with_param(-42, 1,2,3))
    # print(sum_elements_param_with_varargs(-42, 1,2,3))
    print(sum_elements_param_with_varargs(1,2,3, offset=42))
main()