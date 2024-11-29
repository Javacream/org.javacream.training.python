def function_with_string_param(s: str):
    print(s.upper())

def function_with_list_param(l: list[str]):
    first_element = l[0]
    l.append("D")
    first_element.upper()
    return True

def main():
    string = 'Hugo'
    character_list = ['A', 'B', 'S']
    function_with_string_param(string)
    result: bool = function_with_list_param(character_list)
    function_with_list_param(string)
main()