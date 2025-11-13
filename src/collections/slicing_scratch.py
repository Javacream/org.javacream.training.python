numbers = [1, 12, 57, -43, 18, 9]

number_3 = numbers[2]
print(number_3)

# Subliste der Elemente mit Index 2 - 4

# slicing mit ranges wird in Python nicht unterstützt:
# intervall = range(2,4)
# sublist = numbers[intervall]
# sublist = numbers[range(2,4)]

sublist = numbers[2:4]
print(sublist)

sublist = numbers[0:4:2]
print(sublist)

s = 'this is a string'
substring = s[2:4]
print(substring)

# standard-Werte für start, end, step
# step-Standard = 1
# start = 0
# end: Länge der Liste +1
# [:4], [:4:2], [::], 
sublist = numbers[::-1]
print(sublist)
