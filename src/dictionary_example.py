def main():
    # dictionary literal
    postalCodes = {81377: 'München', 40004: 'Hamburg'}

    # iteration über das dict iteriert über die keys
    for key in postalCodes:
        print(key)
    
    for key in postalCodes:
        print(key, postalCodes[key]) # eher untypisch - items() -> weiter unten

    # keys() liefert ein set der keys
    for key in postalCodes.keys():
        print(key)

    # values() liefert ein set der values
    for value in postalCodes.values():
        print(value)

    # items() liefert eine Liste von Tuples der key-value-Paare
    for key, value in postalCodes.items():
        print(key, value)

    # Nebenbemerkung
    items = postalCodes.items()
    x,y = items # items wird quasi auf die beiden Variablen x, y gesplitted
    print(x,y)

    

main()