YOUTH_LIMIT = 18
ADULT_LIMIT = 65

age = input("Geben Sie bitte ihr Alter als ganze Zahl ein: ")
age = int(age)
if age < YOUTH_LIMIT:
    print(f"jugendlich, weil das eingegebenen Alter kleiner als {YOUTH_LIMIT} ist")
elif age >= YOUTH_LIMIT and age <= ADULT_LIMIT:
    print("erwachsen")
else:
    print ("Rentenalter")    

