my_list = ['A', 'B']
my_tuple = tuple(my_list)

my_list = list(my_tuple)

print(my_tuple[1])

if 'A' in my_tuple:
    print(f"'A' is in tuple {my_tuple}")

if 'C' in my_tuple:
    print(f"'C' is in tuple {my_tuple}")
else:
    print(f"'C' is not in tuple {my_tuple}")