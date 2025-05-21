names = ['Hannah', 'Rainer', 'Helga', 'Fritz']

# Aus dieser Liste sollen alle Namen, die mit 'H' beginnen, gefiltert werden

filtered_names = []
for name in names:
    if name.startswith('H'):
        filtered_names.append(name)

# print(filtered_names)

filtered_names = [name for name in names if name.startswith('H')]
 # print(filtered_names)


filtered_and_transformed_names = []
for name in names:
    if name.startswith('H'):
        transformed_name = name.upper()
        filtered_and_transformed_names.append(transformed_name)
print(filtered_and_transformed_names)

filtered_and_transformed_names = [name.upper() for name in names if name.startswith('H')]
print(filtered_and_transformed_names)
