def do_something(l):
    l = ['C']
    # l.append('C')
    print('exiting do_something')

def do_something_with_string(s):
    s = "Emil"
    s2 = s.lower()
    print(s2)
    print('exiting do_something')


def main():
    names = ['A', 'B']
    do_something(names.copy())
    print(names)
    do_something_with_string('Hugo')
main()