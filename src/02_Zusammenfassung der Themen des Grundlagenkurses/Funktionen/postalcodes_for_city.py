def create_data():
    postalcodes_for_city =  {
        'München': ['81371', '81333'],
        'Stuttgart': ['70567'],
        'Berlin': ['30000', '30001', '30002'],
        'Hamburg': ['40005']
    }
    return postalcodes_for_city
def get_city():
    city = input ('please enter a city name: ')
    return city

def search(city, data):
    try:
        return data[city]
    except:
        return None

def write_result(city, postalcodes):
    if postalcodes:
        print(f'postalcodes for {city} are {postalcodes}')
    else:
        print(f'postalcodes for {city} are unknown')
        
def main():
    data = create_data()
    city = get_city()
    postalcodes = search(city, data)
    write_result(city, postalcodes)

main()

