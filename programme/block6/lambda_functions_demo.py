names = ['Hugo', 'Hannelore', 'Andrea', 'Emiliano']

names.sort()
print(names)
names.sort(reverse=True)
print(names)

def length_of_string(s: str) -> int:
    return len(s)
names.sort(key=length_of_string, reverse=True)
print(names)

length_of_string_with_lambda = lambda s : len(s)
names.sort(key=length_of_string_with_lambda)
print(names)

names.sort(key=lambda s : len(s))
print(names)

