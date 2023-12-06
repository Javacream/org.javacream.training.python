def print_to_console(p):
    print('In call: ' + p)
    p = 'Fritz'
    print('In call after reassignement: ' + p)
    return "OK"


def main():
    name = 'Hugo'
    print_to_console(name)
    print('After call: ' + name)
main()