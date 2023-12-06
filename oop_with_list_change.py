def print_to_console(p):
    print('In call: ' + str(p))
    p[0] = 'Emil'
    print('In call after change: ' + str(p))
    return "OK"


def main():
    names = ['Hugo', 'Andrea']
    print_to_console(names)
    print('After call: ' + str(names))
main()