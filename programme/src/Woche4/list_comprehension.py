def without_comprehension(names, character):
    result = []
    for name in names:
        if name.startswith(character):
            result.append(name)
    return result
def with_comprehension(names, character):
    result = [name for name in names if name.startswith(character)]
    return result

def main():
    names = ['Hugo', 'Emil', 'Hannah', 'Hans']
    print(without_comprehension(names, 'E'))
    print(with_comprehension(names, 'H'))

main()