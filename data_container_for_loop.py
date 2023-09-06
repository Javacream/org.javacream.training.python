def loop_with_range():
    # interval = range(5)
    # interval = range(-1, 3)
    # interval = range(5, 1) # sinnlos
    # interval = range(1, 5, 2)
    interval = range(5, 1, -1) 
    for element in interval:
        print(element)

def loop_with_string():
    name = "Hugo"
    for element in name:
        print(element)
def loop_with_tuple():
    seasons = ("Spring", "Summer", "Autumn", "Winter", "Summer")
    for element in seasons:
        print(element)
def loop_with_set():
    names = {"Emil", "Hugo", "Fritz", "Emil"}
    for element in names:
        print(element)

def loop_with_list():
    names = ["Emil", "Hugo", "Fritz", "Emil"]
    for element in names:
        print(element)

#loop_with_tuple()
#loop_with_set()
loop_with_list()

