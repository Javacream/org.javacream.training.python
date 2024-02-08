def main():
    def min_max_with_list(numbers):
        return [min(numbers), max(numbers)]
    def min_max_with_tuple(numbers):
        return (min(numbers), max(numbers))
    def min_max_with_dictionary(numbers):
        return {"min": min(numbers), "max": max(numbers)}
    
    numbers_list = [-3, 7, 8, 42, 0, 666]
    #print(min_max_with_list(numbers_list))
    #print(min_max_with_tuple(numbers_list))
    print(min_max_with_dictionary(numbers_list))

main()