# SLICING

my_list = ['A', 'B', 'C', 'D']
# print(my_list[6])
print(my_list[-1])

my_list[0] = 'C'
print(my_list)
# my_list[42] = 'D'

sub_list = my_list[1:3]
sub_list = my_list[:2] # identisch zu 0:2
sub_list = my_list[1:] # identisch zu 1:4 bzw. besser: 1:len(my_list)
sub_list = my_list[:] # gesamte Liste
sub_list = my_list[:-1]
sub_list = my_list[-1:]
sub_list = my_list[1:4:2]
sub_list = my_list[::-1]

print(sub_list)

