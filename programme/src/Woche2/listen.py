# Erzeugung der Liste mit dem Listen-Literal
todos = ['Einkaufen', 'Putzen', 'Schlafen', 'Essen', 'Putzen']

# Iteration mit for
for entry in todos:
    print(entry)

test_entry = "Joggen"

# if in -Syntax zum Prüfen, ob eine Element vorhanden ist
if test_entry in todos:
    print(f"{test_entry} ist in den todos {todos} enthalten")
else:
    print(f"{test_entry} ist in den todos {todos} nicht enthalten")

# Lesender Indexzugriff
entry = todos[1]
print(entry)

# Schreibender Zugriff ebenfalls über index
todos[1] = 'Entspannen'
print(todos[1])

# Fehler im Zugriff
try:
    print(todos[6])
except Exception as e :
    print("Index 6 ist in der Liste nicht vorhanden")

try:
    todos[6] = 'Trinken'
except Exception as e :
    print("Index 6 ist in der Liste nicht vorhanden")

# Längenbestimmung mit der BuiltIn-Funktion len
print(len(todos))

# Damit Iteration auch über while möglich
todos_length = len(todos)
index = 0
while index < todos_length:
    print(f'{index} = {todos[index]}')
    index +=1 

# Eine Skurrilität: Negative Indizes
print(todos[-3])    

# Slicing
print(todos[2:5])
print(todos[2:5:2])
print(todos[5:2:-1])
sublist = todos[5:2:-1]
print(sublist)
print(todos[:3])
print(todos[3:])
print(todos[:])

