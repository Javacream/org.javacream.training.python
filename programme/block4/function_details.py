def my_function(elements: list[int]):
    print(elements.count(3))


def main():
    n = [1,2,3, 2, 3, 3, 3, 3]
    my_function(n)
    # my_function(42)
main()