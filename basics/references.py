def print_list(l):
    print(l)

def demo_list_reassign(l):
    l = ["A", "B"] # Hier wird der Variable l ein völlig neues Objekt angelegt
    print(l)
    return l

def demo_list_change(l):
    #l[0] = "A" # hier wird über die Referenz l das originale Objekt geändert
    #l[1] = "B"
    l.sort()
    print(l)

def main():
    names = ["Horst", "Helga"]
    # print_list(names)
#    demo_list_reassign(names)
#    demo_list_change(names)
    other_names = names 
    other_names[1] = "Fritz"
    print(names[1]) # Helga oder Fritz??? -> Fritz
    copy_of_names = names.copy()
    copy_of_names[1] = "Hannah"
    print(names[1]) # Fritz oder Hannah??? -> Fritz



main()