def modify_range():
    interval = range(10) 
    #interval[27] = 27 #geht nicht

def modify_set():
    names = {"Emil", "Hugo", "Fritz", "Emil"}
    names2 = {"Helga"}
    names.add("Zvonimir") # Ohne Methoden müsste Python eine Funktion add(names, "Zvonimir")
    print(names)
    print(names2)
    
def modify_list():
    names = ["Emil", "Hugo", "Fritz", "Emil"]
    names.append("Zvonimir") # Ohne Methoden müsste Python eine Funktion add(names, "Zvonimir")
    names[2] = "Rainer"
    print(names)

#modify_range()
modify_list()


