postalCodeToCity = {81371: 'München', 81411: 'München', 76541: 'Stuttgart', 76555: 'Stuttgart'}
cityToPostalCodes = {'München': [81371, 81411], 'Stuttgart': [76541, 76555]}

def add():
    city = input("enter city:")
    code = int(input("enter code:"))
    postalCodeToCity[code] = city
    codesForCity = cityToPostalCodes.get(city)
    if (codesForCity == None):
        codesForCity = []
        cityToPostalCodes[city] = codesForCity
    codesForCity.append(code)

def searchByCity():
    city = input("enter city:")
    print(cityToPostalCodes.get(city))
def searchByCode():
    code = int(input("enter code:"))
    print(postalCodeToCity.get(code))


def __hidden__():
    print ("called hidden function")

