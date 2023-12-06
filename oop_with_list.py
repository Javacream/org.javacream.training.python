def print_to_console(p):
    print('In call: ' + str(p))
    p = ['Fritz', 'Hannah']
    print('In call after reassignement: ' + str(p))
    return "OK"


def main():
    names = ['Hugo', 'Andrea']
    print_to_console(names)
    print('After call: ' + str(names))
main()