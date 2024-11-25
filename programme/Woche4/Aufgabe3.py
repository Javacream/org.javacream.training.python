def string_length_for(strings: list[str]):
    string_length_list = []
    for string in strings:
        string_length_list.append(len(string))
    return string_length_list
def main():
    names = ['Hugo', 'Hannah', 'Andrea']
    result = string_length_for(names)
    print(result)

main()