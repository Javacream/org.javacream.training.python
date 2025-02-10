def size_of(numbers_list):
    return len(numbers_list)
def sum_of(numbers_list):
    return sum(numbers_list) # es gibt tatsächlich hierfür eine BuiltIn-Funktion
def max_of(numbers_list):
    return max(numbers_list)
def min_of(numbers_list):
    return min(numbers_list)
def unique_numbers_of(numbers_list):
    return set(numbers_list)
def duplicates_of(numbers_list):
    unique_numbers = unique_numbers_of(numbers_list)
    duplicates = set()
    for number in numbers_list:
        if numbers_list.count(number) > 1:
            duplicates.add(number)
    return duplicates       
def read_numbers_list(path):
    with open(path) as file:
        rows = file.readlines()
        return [int(row) for row in rows if row != '\n']
def main():
    numbers = read_numbers_list('./numbers.txt')
    print(f'Anzahl Nummern: {size_of(numbers)}')
    print(f'Summe der Nummern: {sum_of(numbers)}')
    print(f'Maximum der Nummern: {max_of(numbers)}')
    print(f'Minimum der Nummern: {min_of(numbers)}')
    print(f'Nummern ohne Duplikate: {unique_numbers_of(numbers)}')
    print(f'Duplikate: {duplicates_of(numbers)}')

main()