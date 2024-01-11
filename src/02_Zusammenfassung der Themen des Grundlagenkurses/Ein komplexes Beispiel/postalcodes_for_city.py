postalcodes_for_city =  {
    'München': ['81371', '81333'],
    'Stuttgart': ['70567'],
    'Berlin': ['30000', '30001', '30002'],
    'Hamburg': ['40005']
}
city = input ('please enter a city name: ')
try:
    print(f'postalcodes for {city} are {postalcodes_for_city[city]}')
except:
    print(f'postalcodes for {city} are unknown')

