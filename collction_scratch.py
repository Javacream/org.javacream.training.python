def print_collection(coll):
    for element in coll:
        print(element)
def main():
    my_set = {"John", "Georg", "Paul", "Ringo", "John"}
    my_list = ["Guitar", "Bass", "Drums", "Guitar"]
    my_dict = {"John": "Rhythm Guitar", "Paul": "Bass", "Ringo": "Drums", "George": "Lead Guitar"}
    my_string = "Beatles"
    my_tuple = (1,2,3)
    #my_tuple = tuple((1,2,3))
    print_collection(my_tuple)
    if 3 in my_tuple:
        print("band has a Mandolin")

main()    