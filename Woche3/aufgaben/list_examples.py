def reverse_list(list):
    list.reverse()
    print(list)
def biggest_and_shortest(list):
    list.sort()
    print(f"Kleinstes: {list[0]}, größtest: {list[len(list) - 1]}")
def remove_duplicates(list):
    no_dups = set(list)
    print(no_dups)
def sum_of_list_elements(list):
    print(sum(list))
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
    numbers = [1, 5, -1, 88, 42, -666]
    sum_of_list_elements(numbers)
    read_csv()
main()