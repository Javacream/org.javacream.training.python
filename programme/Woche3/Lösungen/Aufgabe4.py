# Schnitt und Vereinigung
set1 = {'A', 'B', 'C'}
set2 = {'C', 'D', 'E'}
set3 = {'C', 'A'}
print(set1.intersection(set2))
print(set1.union(set2))

# Submenge
print(set3.issubset(set1))
print(set2.issuperset(set3))

# Duplikate
numbers_list = [1, 3, 22, 3, 22, -33]
numbers_set = set(numbers_list)
numbers_list_without_duplicates = list(numbers_set)
print(numbers_list_without_duplicates)

