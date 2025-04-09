def get_names():
    return ['Emil', 'Hannah', 'Fritz', 'Eduard', 'Andrea', 'Hugo', 'Hans']
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
    print(f'Namen, die mit {filter_char} beginnen: {filtered_names}') 
main()