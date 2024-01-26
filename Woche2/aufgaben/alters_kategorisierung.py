def get_name():
    name = input("Geben Sie Ihren Namen ein: ")
    return name
def get_age():
    age = input("Geben Sie Ihr Alter ein (0 - 125): ")
    age = int(age)
    return age
def get_age_category(p_age):
    if p_age >= 0 and p_age < 18:
        return "jugendlich"
    elif p_age >= 18 and p_age < 65:
        return "erwachsen"
    elif p_age >= 65 and p_age < 125:
        return "im Rentenalter"
    else:
        print(f"Sie haben ein ungültiges Alter eingegeben: {p_age}") 
def print_category(name, category):
    print(f"{name} ist {category}")

def main():
    try:
        name = get_name()
        age = get_age()
        category = get_age_category(age)
        print_category(name, category)
    except:
        print(f"Bitte nur Zahlen eingeben, Sie haben ein ungültiges Alter eingegeben: {age}")     

main()    
