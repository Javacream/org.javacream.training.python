from oop import *
def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    a3 = Address('München', 'Marienplatz')

    print(a1, a2)

    addresses = {a1, a2, a1, a3}
    print(len(addresses))

    address_book = {a1: 'Meier', a2: 'Schneider'}
    print(address_book[a3])

    simple_dict = {'München': 'Meier', 'Stuttgart': 'Schneider'}
    print(simple_dict['Stuttgart'])

if __name__ == '__main__':
    main()