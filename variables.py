# Mit dem # Zeichen wird der Rest der Zeile vom Interpreter ignoriert
# das ist ein Kommentar
# Dieses Programm soll zeigen, wie in Python mit Variablen umgegangen wird


# Analogie zur Tabelle mit Zellen
A1 = "Rainer" # In doppelten Anführungszeichen werden Zeichenketten beliebiger Länge definiert
B1 = 183 # Zahlen werden einfach so eingetragen
C1 = 'Sawitzki' # ein Anführungszeichen gehen auch
# C1 = "Sawitzki' # geht nicht, Anfang und Ende muss das selbe sein
# A2 = 81,3 # Das ist ein subtiler Fehler, A2 wird Zahl zugewiesen! -> später
A2 = 81.7 # jetzt ist es eine Gleitkommazahl

# Besser: Variblen-Namen sind sprechend, "selbst-dokumentierender Code"

firstname = "Rainer"
height = 183
lastname = 'Sawitzki'
weight = 81.7


var_type = type(weight)
print(var_type)

weight = "schwer" # keine strikte Typisierung, eine Variable kann mal eine Zeichenkette sein, mal eine Zahl
var_type = type(weight)
print(var_type)
