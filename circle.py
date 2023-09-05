# this program calculates the rectangle area

def calculate_area(radius):
    return radius * radius * 3.14

def calculate_perimeter(radius):
    return 2 * radius * 3.14

def print_result(area, perimeter):
    print("Area: " + str(area))
    print("Perimeter: " + str(perimeter))

def read_radius():
    return int(input("Input radius: "))
    


def main():
    radius = read_radius()
    area = calculate_area(radius)
    perimeter = calculate_perimeter(radius)
    print_result(area, perimeter)

main()
