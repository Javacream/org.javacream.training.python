n  = input("Bitte Zahl eingeben: ")
n = int(n)

result = dict()
for i in range(1, (n + 1)):
    result[i] = i * i

print(result)

for key in result:
    print(key)


keys = ["81373", "30000", "40000"]
values = ["München", "Berlin", "Hamburg"]

postal_codes = dict()
for index in range(0, len(keys)):
    postal_codes[keys[index]] = values[index]

print(postal_codes)