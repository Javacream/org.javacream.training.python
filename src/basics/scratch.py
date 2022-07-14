names = ["Hugo", "Fritz", "Gregor"]

print(names[1])
names[1] = "Zvonimir"
print(names[1])

names2 = names

names[2] = "Eduardo"
print(names2[2]) #Wirken sich die Änderung in names auch auf names2 aus?
