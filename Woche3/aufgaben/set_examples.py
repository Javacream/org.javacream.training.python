def remove_duplicates(list):
    no_dups = set(list)
    print(no_dups)

def union_and_intersect(set1, set2):
    print(set1.union(set2))
    print(set1.intersection(set2))

def is_subset(set1, set2):
    print(set1.issubset(set2))

def main():
    names = ["Hugo", "Eduard", "Hannah", "Gregor", "Eduard", "Franziska", "Fridolin", "Hugo", "Rudolf", "Hugo"]
    set1 = {"A", "B", "C"}
    set2 = {"C", "D", "E"}
    set3 = {"C", "E"}

    union_and_intersect(set1, set2)
    is_subset(set3, set2)
    is_subset(set3, set1)
    remove_duplicates(names)

main()