postal_codes = {
    '10115': 'Berlin',
    '20095': 'Hamburg',
    '30159': 'Hannover',
    '01067': 'Dresden',
    '04109': 'Leipzig',
    '50667': 'Köln',
    '60311': 'Frankfurt am Main',
    '70173': 'Stuttgart',
    '80331': 'München',
    '90402': 'Nürnberg',
    '28195': 'Bremen',
    '39104': 'Magdeburg',
    '99084': 'Erfurt',
    '55116': 'Mainz',
    '66111': 'Saarbrücken',
    '14467': 'Potsdam',
    '01099': 'Dresden-Neustadt',
    '18055': 'Rostock',
    '17489': 'Greifswald',
    '37073': 'Göttingen',
    '48143': 'Münster',
    '52062': 'Aachen',
    '86150': 'Augsburg',
    '90403': 'Nürnberg-Altstadt',
    '24103': 'Kiel'
}


code = input('please enter a valid postal code: ')
city = postal_codes[code]
print(f'the city for postal code {code} is: {city}')