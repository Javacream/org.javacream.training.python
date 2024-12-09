from people import Address

def main():
    def identity_with_address():
        a1 = Address('A_C', 'A_S')
        a2 = Address('B_C', 'B_S')
        a3 = Address('A_C', 'A_S')

        print(a1 == a2)
        print(a1 == a3)
    def identity_with_str():
        s1 = str('A')
        s2 = str('B')
        s3 = str('A')

        print(s1 == s2)
        print(s1 == s3)

    def duplicate_addresses():
        a1 = Address('A_C', 'A_S')
        a2 = Address('B_C', 'B_S')
        a3 = Address('A_C', 'A_S')
        address_set = {a1, a2, a3}
        print(len(address_set))
    duplicate_addresses()


if __name__ == '__main__':
    main()