todos = ['eat', 'sleep', 'drink']
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

eat_todo = ['eat', 'middle']
sleep_todo = ['sleep', 'low']
drink_todo = ['drink', 'high']

todos_variation1 = [eat_todo, sleep_todo, drink_todo]

todos_variation2 = [['eat', 'middle'], ['sleep', 'low'], ['drink', 'high']]

todos_variation3 = [
    ['eat', 'middle'], 
    ['sleep', 'low'], 
    ['drink', 'high']
]

# Ausgabe der Priorisierung des Eintrags sleep
sleep_todo = todos_variation3[1]
sleep_priority = sleep_todo[1]
print(sleep_priority)
print(todos_variation3[1][1])
# print(todos_variation3[1, 1]) # kann Python nicht

coordinates = [
    ['computer', [
        1,1,3
    ]], 
    'picture', [
        4,5,6
    ]
]

mixed = ['Hugo', [1, 2], True]

if 'Hugo' in mixed:
    print(f'Hugo is in {mixed}')
print('done')