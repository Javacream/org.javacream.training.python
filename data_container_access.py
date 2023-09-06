def access_range():
    interval = range(5, 1, -1) 
    element = interval[0]
    print(element)
def access_string():
    name = "Hugo"
    element = name[0]
    print(element)
def access_tuple():
    seasons = ("Spring", "Summer", "Autumn", "Winter")
    element = seasons[0]
    print(element)

def access_set():
    names = {"Emil", "Hugo", "Fritz", "Emil"}
    #element = names[0] # kein Index für Sets!
    # print(element)


#access_range()
#access_string()
#access_tuple()
access_set()