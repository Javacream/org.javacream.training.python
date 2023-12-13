def fixed_parameter_list(p1, p2):
    pass
 
fixed_parameter_list('A', 42)
#fixed_parameter_list('A') TypeError
 
def varargs(p1, *p2): # p2 ist ein iterierbares Tupel
    print(p1)
    for param in p2:
        print(param)
#varargs('A', 42)
#varargs('A')
#varargs('A', 47, 11, True, 'Egal')
 
def kwargs(p1, **p2): # p2 ist ein Dictionary
    print(p1, p2)
 
 
kwargs("A", dies="Das", anything="else") # Sawitzki: Besser wäre {dies: "Das", anything: "else"}