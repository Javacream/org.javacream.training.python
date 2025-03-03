city_for_postalcode =  {
    '81371': 'München',
    '70567': 'Stuttgart',
    '30000': 'Berlin',
    '81333': 'München',
    '30001': 'Berlin',
    '30002': 'Berlin',
    '40005': 'Hamburg'
}
postalcode = input ('please enter a 5 digit postal code: ')
try:
    print(f'city for postalcode {postalcode} is {city_for_postalcode[postalcode]}')
except:
    print(f'city for postalcode {postalcode} not found')

