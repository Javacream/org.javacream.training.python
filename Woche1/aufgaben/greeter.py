try:
    name = input("Bitte gebe deinen Namen ein: ")
    age = input("Bitte dein Alter ein (nur Zahlen zwischen 0 und 125): ")
    age = int(age)
    if age < 0 or age > 150:
        print(f"Du hast ein ungültiges Alter eingegeben: {age}")
    else:
        print(f"Hallo {name}, du bist {age} Jahre alt")
except:
    print("Dein Alter ist keine Zahl: {age}")
