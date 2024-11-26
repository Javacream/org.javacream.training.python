names = ['Hugo', 'Andrea', 'Hannah', 'Gregor', "Emiliana", 'Harald']

# ___________________________

result = []

for name in names:
    if name.startswith('H'):
        result.append(len(name))


# ___________________________
comprehension_result = [len(name) for name in names if name.startswith('H')]
print('done')