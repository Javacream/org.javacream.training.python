keys = ["81373", "30000", "40000"]
values = ["München", "Berlin", "Hamburg"]

postal_codes = dict()
for index in range(0, len(keys)):
    postal_codes[keys[index]] = values[index]

print(postal_codes)