todos = ('eat', 'sleep', 'drink')
todos = 'eat', 'sleep', 'drink'

print(len(todos))

# Anstoßen einer Konsolenausgabe
print(42)

# Anstoßen einer Aktion, die aus einer Liste den gewählten Index bestimmt
# todos(1) nicht korrekt
second_item = todos[1]
print(second_item)
print(todos[0])

# Neuer Schleifentyp: for in
# Allgemein: Das Aufzählen der Elemente nennt man Iteration
for todo in todos: # Die Zuweisung an die Variable todo erfolgt automatisch intern für jeden Durchlauf mit dem jeweils neuen Element
    print(todo)

for item in todos:
    print(item)
for x in todos:
    print(x)

todo1, todo2, todo3 = todos

print('done')