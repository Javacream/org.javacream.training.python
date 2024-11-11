user_input = input('Bitte eine Zahl eingeben: ')
number = int(user_input) # Hier wird der ValueError "geworfen" 
print(2 * number) # dies wird nicht mehr ausgeführt, der geworfene Fehler verhindert die Ausführung der nächsten Zeile
