def tuple_to_list_and_back(elements):
    list_from_tuple = list(elements)
    tuple_from_list = tuple(list_from_tuple)
    print(list_from_tuple)
    print(tuple_from_list)

def element_of_tuple(elements, index):
    print(elements[index])

def element_in_tuple(elements, check):
    print(f"{check} in {elements}: {check in elements}")
def main():
    seasons = tuple(["Winter", "Frühling", "Sommer", "Herbst"])
    tuple_to_list_and_back(seasons)
    element_of_tuple(seasons, 3)
    element_in_tuple(seasons, "Sommer")
    element_in_tuple(seasons, "Fasching")

main()