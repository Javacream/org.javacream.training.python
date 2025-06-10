def tuple_sample():
    seasons = ('winter', 'spring', 'summer', 'automn')

    print(seasons[1])
    for season in seasons:
        print(season)

def set_sample():
    # my_collection = ['Hugo', 'Hannah', 'Egon', 'Hugo', 'Andrea'] # so ist es eine Liste
    my_collection = {'Hugo', 'Hannah', 'Egon', 'Hugo', 'Andrea'} # so ist es ein Set
    print(len(my_collection))
    # my_collection[0]
    my_collection.add('Hugo')
    print(len(my_collection))

    for name in my_collection:
        print(name)

def collections_builtins():
    my_range = range(1, 5, 2)
    coll = list() # []
    coll = dict() # {}
    coll = set() # {} kein set!
    coll = tuple() # ziemlich sinnlos, aber möglich
    my_collection = ['Hugo', 'Hannah', 'Egon', 'Hugo', 'Andrea']
    my_collection_as_set = set(my_collection)
    my_collection_as_tuple = tuple(my_collection)
    
    name = 'Sawitzki'
    name_set = set(name)
    name_set2 = {name}

    name_list = list(name)
    print(name_set)
    print(name_set2)
    print(name_list)
    # my_dict = dict(my_collection)
def main():
    # tuple_sample()
    # set_sample()
    collections_builtins()
main()

