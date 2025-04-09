def get_names(): 
    with open('programme/src/Woche4/names.txt', 'rt', encoding='utf-8') as input_file:  
        raw_names = input_file.readlines()
        names = []
        for raw_name in raw_names:
            if raw_name.endswith('\n'):
                names.append(raw_name[:-1])
            else:
                names.append(raw_name)
        return names
def get_character():
    str = input("Geben Sie einen Buchstaben ein: ")
    return str[0]
def names_starting_with(names, character):
    result = []
    for name in names:
        if name.startswith(character):
            result.append(name)
    return result
def main():
    names = get_names()
    filter_char = get_character()
    filtered_names = names_starting_with(names, filter_char)
    for index in range(0, len(filtered_names)):
        filtered_names[index] += '\n'
    with open (f'programme/src/Woche4/names_filtered_by_{filter_char}.txt', 'wt', encoding='utf-8') as outfile:
        outfile.writelines(filtered_names)
main()