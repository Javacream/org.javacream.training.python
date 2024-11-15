names = ['Hugo', 'Hannelore', 'Andrea', 'Lea']
names.sort()
print(names)
names.sort(reverse=True)
print(names)

def name_length(name):
    return len(name)

names.sort(key=name_length)
print(names)

name_length = lambda name : len(name)
names.sort(key=name_length)
print(names)

names.sort(key=lambda name : len(name))
print(names)
