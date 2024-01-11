def a_function_that_modifies_a_list_param(a_list):
    a_list.clear()

def a_function_that_redefines_a_parameter(a_list):
    a_list = []

def main():
    names=['Hugo', 'Emil']
    a_function_that_modifies_a_list_param(names)
    print(len(names)) # 0
    names=['Hugo', 'Emil']
    a_function_that_redefines_a_parameter(names)
    print(len(names)) # 2

main()
