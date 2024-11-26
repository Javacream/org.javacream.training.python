value_list = [1,2,3,5,8,13,21,44,85]
key_list = "fibonacci"

result = dict()
index = 0
for key in key_list:
    result[key] = value_list[index]
    index += 1

tuples = result.items()
print(tuples)