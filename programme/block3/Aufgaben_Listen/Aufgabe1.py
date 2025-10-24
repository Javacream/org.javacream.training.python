todos = ['Einkaufen', 'Putzen', 'Schlafen', 'Essen', 'Putzen']

start = len(todos) - 1
end = 0
index = start
while index <= start:
    print(todos[index])
    index -= 1
    if index < 0:
        break

todos_reversed = reversed(todos)
for todo in todos_reversed:
    print(todo)


todos_reversed_slice = todos[::-1]
for todo in todos_reversed_slice:
    print(todo)

