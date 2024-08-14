MIN_AGE = 0
MAX_AGE = 125

YOUTH_LIMIT = 18
ADULT_LIMIT = 65

AGE_INPUT_MESSAGE = "Geben Sie bitte ihr Alter als ganze Zahl ein: "
YOUTH_MESSAGE = f"jugendlich, weil das eingegebenen Alter kleiner als {YOUTH_LIMIT} ist"
ADULT_MESSAGE = "erwachsen"
RETIRED_MESSAGE = "Rentenalter"


age = input(AGE_INPUT_MESSAGE)
age = int(age)

INVALID_AGE_MESSAGE = f"ungültiges Alter: {age}"

if age < MIN_AGE or age > MAX_AGE:
    print(INVALID_AGE_MESSAGE)
else:
    if age < YOUTH_LIMIT:
        print(YOUTH_MESSAGE)
    elif age >= YOUTH_LIMIT and age <= ADULT_LIMIT:
        print(ADULT_MESSAGE)
    else:
        print (RETIRED_MESSAGE)    

