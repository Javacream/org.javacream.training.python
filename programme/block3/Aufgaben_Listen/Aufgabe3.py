todos = ['Einkaufen', 'Putzen', 'Schlafen', 'Essen', 'Putzen']
result = []
for todo in todos:
    if not todo in result:
        result.append(todo)

print(result)

todos_set = set(todos)
result = list(todos_set)
print(result)