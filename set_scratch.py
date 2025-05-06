numbers = {1, 3, 42, -9, 5, 42, 42}
print(type(numbers))
print(len(numbers))
# print(numbers[0]) # 'set' object is not subscriptable
for number in numbers:
    print(number)

print(33 in numbers)    