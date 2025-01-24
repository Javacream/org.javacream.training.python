number = 42

number = number + 2

# number('Hugo') not callable, also keine Funktion
# number[1] not subscriptable, also keine Collection

print("Hello")
# print = print + 2 Ich kann Funktion nichts addieren

# print[1] # not subscriptable, also keine Collection

person1 = ['Sawitzki', 'Rainer']
# person1 = person1 + 2 Zu einer Liste kann keine Zahl addiert werden
# person1('Hugo') not callable, also keine Funktion

second_element = person1[1]
print(second_element)

person2 = ['Musterperson', 'Andrea', 176]

print(len(person1), len(person2))

for element in person2:
    print(element)

# Möglich, aber völlig untypisch
index = 0
while index < len(person2):
    print(person2[index])
    index += 1     
