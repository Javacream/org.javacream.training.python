def print_collection(coll):
    for element in coll:
        print(element)
def main():
    my_set = {"John", "Georg", "Paul", "Ringo", "John"}
    my_list = ["Guitar", "Bass", "Drums", "Guitar"]
    my_dict = {"John": "Rhythm Guitar", "Paul": "Bass", "Ringo": "Drums", "George": "Lead Guitar"}
    print_collection(my_dict)
    if "Mandolin" in my_list:
        print("band has a Mandolin")

main()    