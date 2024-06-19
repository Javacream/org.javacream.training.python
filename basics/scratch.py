# Slicing
names = ["A", "B", "C", "D", "E"]
name = names[1] # Zugriff ein Element
start_index = 1
end_index = 3
sub_list = names[start_index:end_index]
print(sub_list)
sub_list = names[0:3] #-> 0 ist der Standard!
sub_list = names[:3]
sub_list = names[1:len(names)] #-> len(liste) ist der Standard!
sub_list = names[1:]
names[-1] # -> E 
names[0:len(names) - 1] 
names[:-1] # -> E 
