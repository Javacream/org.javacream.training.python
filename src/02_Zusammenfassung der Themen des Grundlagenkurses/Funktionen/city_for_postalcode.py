def create_data():
    city_for_postalcode =  {
        '81371': 'München',
        '70567': 'Stuttgart',
        '30000': 'Berlin',
        '81333': 'München',
        '30001': 'Berlin',
        '30002': 'Berlin',
        '40005': 'Hamburg'
    }
    return city_for_postalcode

def get_postal_code():
    postalcode = input ('please enter a 5 digit postal code: ')
    return postalcode

def search_city(postalcode, data):
    try:
        return data.get(postalcode)
    except:
        return None

def write_result(postalcode, city):
    if city:
        print(f'city for postalcode {postalcode} is {city}')
    else:
        print(f'city for postalcode {postalcode} not found')

def main():
    data = create_data()
    postalcode = get_postal_code()
    city = search_city(postalcode, data)
    write_result(postalcode, city)

main()
