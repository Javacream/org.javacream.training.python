def sum_elements(numbers):
    return sum(numbers)

def sum_elements2(*numbers):
    return sum(numbers)

def main():
    n = (1, 5, 2, -4, 3)
    print(sum_elements(n))
    print(sum_elements2(1, 5, 2, -4, 3))

main()