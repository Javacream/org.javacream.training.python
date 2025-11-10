names = ['Hugo', 'Andrea', 'Emilian']

names.sort()
print(names)

names.sort(reverse=True)
print(names)

def sort_by_stringlength(s: str):
    return len(s)

names.sort(key = sort_by_stringlength)
print(names)

names.sort(key = lambda s: -len(s))
print(names)

