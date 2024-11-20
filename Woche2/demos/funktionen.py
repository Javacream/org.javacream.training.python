# die folgenden beiden Zeilen realisieren eine Benutzereingabe eines Alters als Zahl
#user_input = input("Bitte geben Sie eine Zahl ein: ")
#age = int(user_input)

# Als Einzeiler werden die beiden Aktionen gruppiert
# Das ist zu vermeiden, wird total schnell unübersichtlich und schwierig zu debuggen
#age = int(input("Bitte geben Sie eine Zahl ein: ")) 

def name_input():
    user_input = input("Bitte geben Sie Ihren Namen ein: ")
    return user_input


def age_input():
    user_input = input("Bitte geben Sie eine Zahl ein: ")
    age = int(user_input)
    return age

# Eine Benutzer-Eingabe von Name und Alter soll zu einer kategorisierten Ausgabe führen: Name ist 'jung', 'erwachsen, 'alt'
def main():
    name = name_input()
    age = age_input()
    print(f"{name} ist {age} Jahre alt")

main()


