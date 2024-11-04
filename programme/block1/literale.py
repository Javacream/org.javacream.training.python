# Literale werden in der rechten Seite einer Zuweisung benutzt

lastname = "Sawitzki" # "" -> Zeichenkette mit beliebigen Zeichen in beliebiger Länge
# Falsch: Literalen können keine Werte zugewiesen werden
#"Sawitzki" = "Hugo"

firstname = 'Rainer' # '' -> Zeichenkette mit beliebigen Zeichen in beliebiger Länge

# Warum "" und '': 
# var_with_quotation = "Der Name "Sawitzki" entstammt" 
var_with_quotation = 'Der Name "Sawitzki" entstammt'
var_with_quotation = "Der Name 'Sawitzki' entstammt"
var_with_escaped_quotation = "Der Name \"Sawitzki\" entstammt" 
print(var_with_escaped_quotation)

int_number = 183 # 42 ist ein Ganzzahl-Literal
float_number = 74.8 # 4.2 ist eine Kommazahl, Vorsicht: Trennzeichen ist der .

# True und False sind boolsche Literale -> später bei der Besprechung von Abfragen
real = True
wrong = False

# Zur Vollständigkeit: Es existieren Literale für Listen, Mengen, Nachschlage-Tabellen, reguläre Ausdrücke

# Zeichenketten-Interpolation = Zugriff auf Variablen innerhalb einer Zeichenkette

sawitzki_info = f"{firstname} {lastname} ist {int_number}cm groß und {float_number}kg schwer"

print(sawitzki_info)