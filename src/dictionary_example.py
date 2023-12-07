def main():
    # dictionary literal
    postalCodes = {81377: 'München', 40004: 'Hamburg'}
#    city = postalCodes[40009]
#    print(city)

    def own_dict(key):
        if key == 81377:
            return 'München'
        elif key == 40004:
            return 'Hamburg'
        else:
            raise KeyError()
    
    city = own_dict(40009)
    print(city)
main()