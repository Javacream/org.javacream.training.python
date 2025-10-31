def sum_elements(numbers):
    return sum(numbers)

def sum_elements2(*numbers):
    return sum(numbers)

def sum_elements3(*numbers, offset, multiplier):
    return multiplier*(offset + sum(numbers))


def main():
    print(sum_elements3(1, 2, 3, 4, offset=42, multiplier=-1))
main()