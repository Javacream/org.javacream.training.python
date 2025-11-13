names = ('Hugo', 'Emil', 'Andrea', 'Hugo')

print(type(names))

unique_names = set(names)
print(unique_names)

frozen_unique_names = tuple(unique_names)

print(type(frozen_unique_names))
print(frozen_unique_names)
