names = ['Hugo', 'Andrea', 'Paula', 'Hannah', 'John', 'Holly']
names.sort()
print(names)

def sort_key(element):
    return len(element)

names.sort(key=sort_key)
print(names)

names.sort(key=lambda name: name[-1])
print(names)
