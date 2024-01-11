def reverse_list(list):
    list.reverse() # list[::-1]
    print(list)
def biggest_and_shortest(list):
    list.sort() # max(list), min(list) ist eine alternative Lösung
    print(f"Kleinstes: {list[0]}, größtest: {list[len(list) - 1]}")
def remove_duplicates(list):
    no_dups = set(list)
    print(no_dups)
def sum_of_list_elements(list):
    print(sum(list))
def sum_of_list_elements_variante2(list):
    print(type(list[0]))
    if type(list[0]) == type(" "):
        sum = ""
    else:
        sum = 0    
    for element in list:
        sum = sum + element
    print(sum)

def read_csv():
    with open("Woche3/aufgaben/names.csv") as file:
        rows = file.readlines()
        result = []
        for row in rows:
            row = row.replace("\n", "")
            result.append(row.split(","))
        print(result)    
def main():
    names = ["Hugo", "Eduard", "Hannah", "Gregor", "Eduard", "Franziska", "Fridolin", "Hugo", "Rudolf", "Hugo"]
    reverse_list(names)
    biggest_and_shortest(names)
    remove_duplicates(names)
    numbers = [1, 5, -1, 88, 42, -6.66]
    sum_of_list_elements(numbers)
    read_csv()
    sum_of_list_elements_variante2(names)
main()