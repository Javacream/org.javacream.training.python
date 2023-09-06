def containers():
    interval = range(10) 
    name = "Fridolin"
    seasons = ("Spring", "Summer", "Autumn", "Winter")
    names = {"Emil", "Hugo", "Fritz", "Emil"}
    names_list = ["Emil", "Hugo", "Fritz", "Emil"]
    print_container_length(interval)
    print_container_length(name)
    print_container_length(seasons)
    print_container_length(names)
    print_container_length(names_list)

def print_container_length(container):
    length = len(container)
    print(length)

containers()

