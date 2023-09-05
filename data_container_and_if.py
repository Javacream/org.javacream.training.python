def check_range():
    interval = range(5, 1, -1) 
    if 3 in interval:
        print("3 is in interval")
def check_string():
    name = "Hugo"
    if 'u' in name:
        print("u is in name")
def check_tuple():
    seasons = ("Spring", "Summer", "Autumn", "Winter")
    if "Summer" in seasons:
        print("Summer is in seasons")

check_range()
check_string()
check_tuple()
