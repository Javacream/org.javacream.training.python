names = ['Hugo', 'Andrea', 'Paula', 'Hannah', 'John', 'Holly']

result = []
for name in names:
    if name.startswith('H'):
        name_length = len(name)
        result.append(name_length)

result = [len(name) for name in names if name.startswith('H')]
