age = input("Geben Sie bitte ihr Alter als ganze Zahl ein: ")
age = int(age)
if age < 18:
    print("jugendlich")
elif age >= 18 and age <= 65:
    print("erwachsen")
else:
    print ("Rentenalter")    

