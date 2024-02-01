def squared(n):
    squared_numbers = dict()
    for i in range(1, n + 1):
        squared_numbers[i] = i*i
    print(squared_numbers)
    return squared_numbers
def print_keys(dictionary):
    for key in dictionary.keys():
        print(key)

def dict_from_two_lists(l1, l2):
    result = dict()
    size = len(l1)
    for i in range(size):
        result[l1[i]] = l2[i]
    print(result)
    return result

def sum_of_values_in_dict(dictionary):
    print(sum(dictionary.values()))

def dict_to_tuple_list(input_dict):
    tuple_list = [(key, value) for key, value in input_dict.items()]
    print(tuple_list)

def key_in_dict(key, dictionary):
    value = dictionary.get(key)
    if (value == None):
        print(f"{key} is not in dictionary {dictionary}")
    else:
        print(f"{key} is in dictionary {dictionary}")
def main():
    n = int(input("Bitte eine Zahl eingeben: "))
    test_dict = squared(n)
    print_keys(test_dict)
    list1 = ["A", "B", "C"]
    list2 = [1, 2, 42]

    test_dict = dict_from_two_lists(list1, list2)
    sum_of_values_in_dict(test_dict)
    dict_to_tuple_list(test_dict)
    key_in_dict("B", test_dict)
    key_in_dict("Z", test_dict)

main()