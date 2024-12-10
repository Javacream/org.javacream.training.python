from people import Address
def main():
    a1 = Address('München', 'Marienplatz')
    a2 = Address('Berlin', 'Alexanderplatz')
    a3 = Address('München', 'Marienplatz')

    address_set = {a1, a2, a3}
    print(len(address_set))
if __name__ == '__main__':
    main()