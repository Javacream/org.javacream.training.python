def main():
    # dictionary literal
    postalCodes = {81377: 'München', 40004: 'Hamburg'}
    postalCodes[40009] = 'Hamburg'
    postalCodes[30000] = 'Barlin'
    postalCodes[30000] = 'Berlin'
    print(len(postalCodes))

main()