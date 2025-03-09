def main():
    set1 = {'a', 'b', 'c', 'd'}
    set2 = {'c', 'a'}
    set3 = {'c', 'f'}
    set3_is_subset_of_set1 = set1.issuperset(set3)
    print(f'Is set2 {set2} a subset of set1 {set1}: {set2.issubset(set1)}')
    print(f'Is set3 {set3} a subset of set1 {set1}: {set3_is_subset_of_set1}')
main()
