postalCodeToCity = {81371: 'München', 81411: 'München', 76541: 'Stuttgart', 76555: 'Stuttgart'}
print(postalCodeToCity[81371])

cityToPostalCodes = {'München': [81371, 81411], 'Stuttgart': [76541, 76555]}

for postalCode in cityToPostalCodes['München']:
    print(postalCode)


def createPerson(lastname, firstname):
    return (lastname, firstname)

sawitzki = createPerson("Sawitzki", "Rainer")
print(sawitzki)