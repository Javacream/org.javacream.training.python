names = ['Hugo', 'Emil', 'Andrea', 'Hugo']

# Kopie der ursprünglichen Liste

copy_of_names = [name for name in names]
print(copy_of_names)

transformation_of_names = [f'*** {name} ***' for name in names]
print(transformation_of_names)

filtered_names = [name for name in names if name[0] == 'A']
print(filtered_names)

transformed_and_filtered_names = [f'*** {name} ***' for name in names if name[0] == 'A']
print(transformed_and_filtered_names)

copy_of_names = {name for name in names}
print(copy_of_names)

copy_of_names = tuple(name for name in names)
print(copy_of_names)
