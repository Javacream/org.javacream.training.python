def main():
    def sum_of_list_with_list(numbers_list):
        sum_of_list = sum(numbers_list)
        print(sum_of_list)

    def sum_of_list_with_varargs(*args):
        sum_of_list = sum(args)
        print(sum_of_list)

    numbers = [1,2,3,42]
    sum_of_list_with_list(numbers)
    sum_of_list_with_varargs(1,2,3,4,5)

main()