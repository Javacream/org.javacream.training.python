def number_of_characters(string: str):
    return len(string)

def number_of_character(char:str , string: str):
    return string.count(char)

def number_of_words(string: str):
    return len(string.split(' '))

def is_int(string: str):
    return string.isdigit()

def is_float(string: str):
    if string.count('.') > 1:
        return False
    else:
        string = string.replace('.', '')
    return string.isdigit()

def main():
    test_string = 'Hello my friend'
    print(f'numbers of characters: {number_of_characters(test_string)}')
    print(f'numbers of character e: {number_of_character('e', test_string)}')
    print(f'numbers of words: {number_of_words(test_string)}')
    test_int_string = '123'
    print(f'is 123 numeric: {is_int(test_int_string)}')
    print(f'is 12x3 numeric: {is_int("12x3")}')
    test_float_string = '12.3'
    print(f'is 12.3 numeric: {is_float(test_float_string)}')
    print(f'is 1.2.3 numeric: {is_float("1.2.3")}')


main()