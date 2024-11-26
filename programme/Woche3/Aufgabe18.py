postal_codes = {'81373': 'München', '70567': 'Stuttgart'}

code = '81373'
value = postal_codes.get(code)
if value != None:
    print(f'code {code} found')
else:
    print(f'code {code} not found')

code = '99999'
value = postal_codes.get(code)
if value != None:
    print(f'code {code} found')
else:
    print(f'code {code} not found')