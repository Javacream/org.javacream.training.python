def get_name():
    name = input("Geben Sie Ihren Namen ein: ")
    return name
def get_age():
    age = input("Geben Sie Ihr Alter ein (0 - 125): ")
    age = int(age)
    return age
def print_age_category(p_name, p_age):
    if p_age >= 0 and p_age < 18:
        print(f"{p_name} ist jugendlich")
    elif p_age >= 18 and p_age < 65:
        print(f"{p_name} ist erwachsen")
    elif p_age >= 65 and p_age < 125:
        print(f"{p_name} ist im Rentenalter")
    else:
        print(f"Sie haben ein ungültiges Alter eingegeben: {p_age}")     
    return "OK"        
def main():
    try:
        name = get_name()
        age = get_age()
        print_age_category(name, age)
    except:
        print(f"Bitte nur Zahlen eingeben, Sie haben ein ungültiges Alter eingegeben: {age}")     

main()    