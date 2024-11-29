from math import pi as circle_number, sqrt as square_root

def radius_from_area(area: float):
    result = square_root(area/circle_number)
    return result


def perimeter(radius: float):
    result = 2 * radius * pi
    return result

def main():
    print(perimeter(2.2))
    print(radius_from_area(4.2))

main()