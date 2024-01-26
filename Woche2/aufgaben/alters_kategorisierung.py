def main():
    name = input("Geben Sie Ihren Namen ein: ")
    try:
        age = input("Geben Sie Ihr Alter ein (0 - 125): ")
        age = int(age)
        if age >= 0 and age < 18:
            print(f"{name} ist jugendlich")
        elif age >= 18 and age < 65:
            print(f"{name} ist erwachsen")
        elif age >= 65 and age < 125:
            print(f"{name} ist im Rentenalter")
        else:
            print(f"Sie haben ein ungültiges Alter eingegeben: {age}")             
    except:
        print(f"Bitte nur Zahlen eingeben, Sie haben ein ungültiges Alter eingegeben: {age}")     

main()    