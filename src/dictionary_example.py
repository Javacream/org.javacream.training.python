def main():
    # dictionary literal
    postalCodes = {81377: 'München', 40004: 'Hamburg'}
    postalCodes[40009] = 'Hamburg'
    postalCodes[30000] = 'Barlin'
    postalCodes[30000] = 'Berlin'
    print(len(postalCodes))

    plz = 81379
    city = postalCodes.get(81379)
    if city != None:
        print(city)
    else:
        print(f'city for {plz} not found')    

    postalCodes.setdefault(70000, 'Stuttgart') #Sawitzki: besser wäre der name set_or_update
    print(len(postalCodes))
    update_dict = {70001: 'Stuttgart', 81377: 'Augsburg'}
    postalCodes.update(update_dict) #Parameter ist ein Dictionary, das die neuen key-value-Paare enthält, Sawitzki: besser merge
    print(len(postalCodes))
    print(postalCodes.get(81377))

main()