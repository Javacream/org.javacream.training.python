my_range = range(1,6)

print(my_range[3])

my_range = range(1,6,2)

my_range = range(6,1,-1)

for number in my_range:
    print(number)

print(my_range[-1])
#identisch zu
print(my_range[len(my_range) - 1])

candidate = 2
if candidate in my_range:
    print(f'{candidate} is in {my_range}')
