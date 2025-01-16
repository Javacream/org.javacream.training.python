MIN_ADULT_AGE = 18
MAX_ADULT_AGE = 65

name = input('Bitte geben Sie Ihren Namen an: ')
age = input(f'{name}, geben Sie bitte ihr Alter an: ')
age = int(age)

if age < MIN_ADULT_AGE:
    age_category = "jugendlich"
elif age < MAX_ADULT_AGE:
    age_category = "erwachsen"
else:
    age_category = 'im Rentenalter'    

print(f'{name} ist {age_category}')
