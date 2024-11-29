import math as math_utilities

def perimeter(radius: float):
    result = 2 * radius * math_utilities.pi
    return result

def main():
    print(perimeter(2.2))


main()