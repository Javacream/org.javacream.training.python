input_text = input("Bitte etwas eingeben: ")
# if-Statement: Prüfe, ob die Eingabe als Zahl interpretierbar ist -> aufwändig
try:
    number = int(input_text)
    print(f"Zahl ist {number}")
except:
    print(f"{input_text} is not a valid number")

# SyntaxError kann nicht behandelt werden
#try:
#    message = "Hugo
#except SyntaxError:
#    print("das programm ist syntaktisch falsch")    
